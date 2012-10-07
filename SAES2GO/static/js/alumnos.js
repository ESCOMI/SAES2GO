$(document).ready(function (){
			
	$("#dvNav ul li").hover(
       function()
       {		          	
			$(this).addClass("sobreMenu");
       },
       function()
       {
           	$(this).removeClass("sobreMenu");
       }
    );

    var $materiaClonada = null;
    var $targetsMateria = null;
    var materiasGrupo = {};

    var coloresValidos = ["#FF6600","#E0AE49","#F24343","#FF88AA","#44A0FD","#40A640","#00CCCC"
    ,"#B0B0B0","#FB439F","#BB77DD","#C06D58","#DE00ED","#77AADD","#336666","#660000"];

    $("#dvNav ul li").click(
       function()
       {                    
            $.get("/alumnos/"+$(this).data("view")+"/",function  (html) {

              $(".rightPane").html(html);


              var $horarios = $("#dvHorarios table tr");

              $horarios.filter(".matutino").hide();

              $targetsMateria = $("#dvHorarios").find("table > tbody > tr > td > div");



              function prepareTargets($targetsMateria){

                $targetsMateria.click(function () {

                  if($materiaClonada != null){
                    
                    $nuevoDiv = $("<div>");
                    $nuevoDiv.attr("data-id-materia",$materiaClonada.attr("data-id-materia"));
                    $nuevoDiv.attr("data-horas-materia",$materiaClonada.attr("data-horas-materia"));
                    $nuevoDiv.html( $materiaClonada.html() );
                    $nuevoDiv.css("backgroundColor",$materiaClonada.css("backgroundColor"));
                    $nuevoDiv.click(function () {                  
                          
                          materiasGrupo [$materiaClonada.attr("data-id-materia")] = buscaHorarioSimilares ($(this),"q");

                    })

                    $(this).replaceWith($nuevoDiv);  

                    materiasGrupo [$materiaClonada.attr("data-id-materia")] = buscaHorarioSimilares ($materiaClonada,"a");

                  }

                });

              }
              
              $("#btnLimpiarHorario").click(function (){                
                $horarios.find("div").replaceWith("<div></div>");
              });


              $("#btnGuardarHorario").click(function (){
                $.getJSON("/grupos/guardar/",{
                  grupo:$("#cmbGrupos").val(),
                  salon:$("#txtSalon").val(),
                  materias:JSON.stringify(materiasGrupo)
                },function (resultado) {
                  
                });

              });


              // Se consultan las materias filtrando por nivel
              $("#cmbNiveles").change(function (){                  

                if($(this).val() == -1) return false;
                
                $.getJSON("/materias/",{nivel:$(this).val()},function  (materias) {

                 
                  var arrayMaterias = [];

                  $.each(materias,function (index, materia) {                    
                    arrayMaterias.push("<li data-id-materia=\"mat"+materia.id+"\" data-horas-materia=\""+materia.horas+"\" style=\"background-color:"+coloresValidos[index]+"\">"+materia.nombre+"</li>")

                  });

                  $("#tiraMaterias").empty().append(arrayMaterias.join("")).find("li").click(function () {
                      
                      $(this).siblings().removeClass("over") 
                      $(this).addClass("over");

                      $materiaClonada =  $(this).clone();
                      $materiaClonada.css("backgroundColor",$(this).css("backgroundColor"));

                      buscaHorarioSimilares($materiaClonada,"a");    

                      $targetsMateria.not("[data-id-materia]").attr("class","target");

                  });


                  prepareTargets($targetsMateria);

                });

              });

              //Se consultan los grupos
              $("#cmbTurno").change(function (){ 

                $("#cmbGrupos option:not(:first)").remove();

                $.getJSON("/grupos/",{turno:$(this).val()},function  (grupos) {

                  var arrayGrupos = [];

                  $.each(grupos,function (index, grupo) {
                    
                    arrayGrupos.push("<option value=\""+grupo.nombre+"\">"+grupo.nombre+"</option>");

                  });

                  $("#cmbGrupos").append(arrayGrupos.join("")).change(function () {
                    
                    if($(this).val() == -1) return false;

                    var $horarios = $("#dvHorarios").find("table tbody tr")

                    if($(this).val().toLowerCase().indexOf("v") > -1){
                      $horarios.filter(".matutino").hide();
                      $horarios.filter(".vespertino").show();
                    }else{
                      $horarios.filter(".vespertino").hide();
                      $horarios.filter(".matutino").show();
                    }

                  })

                });

              }); 

              

              var tiposHorario = [];
               //Se consultan los tipos de horario validos
              $.getJSON("/tiposHorario/",function  (horarios) {

                $.each(horarios,function (index, horario) {
                  var campos = horario.fields;
                  

                  var arrHorarios = [];

                  arrHorarios.push("h"+campos.horaLunes+"-"+campos.duracionLunes);
                  arrHorarios.push("h"+campos.horaMartes+"-"+campos.duracionMartes);
                  arrHorarios.push("h"+campos.horaMiercoles+"-"+campos.duracionMiercoles);
                  arrHorarios.push("h"+campos.horaJueves+"-"+campos.duracionJueves);
                  arrHorarios.push("h"+campos.horaViernes+"-"+campos.duracionViernes); 
                  tiposHorario.push({id:horario.pk,horario:arrHorarios});

                });

              });


              
              

              function buscaHorarioSimilares (materia,agregarQuitar) {

                var horasXSemana = parseFloat(materia.attr("data-horas-materia"));
                var $materiasAgregadas = $horarios.find("div[data-id-materia="+materia.attr("data-id-materia")+"]");
                
                if(agregarQuitar=="q")
                  materia.replaceWith("<div class=\"target\"></div>");
                //Si se esta quitando la ultima
                if($materiasAgregadas.size() == 1 && agregarQuitar=="q"){
                  
                  $horarios.find("div:not([data-id-materia])").replaceWith("<div class=\"target\"></div>");
                  prepareTargets($horarios.find(".target"));
                  return null;
                }               
                  

                var arrMateriasAgregadas = ["","","","",""];

                $.each($materiasAgregadas,function () {

                  arrMateriasAgregadas[$(this).parent().index()-1] = $(this).parent().parent().attr("data-hora-inicio")+"-90";

                });
                
                var coincidentes = [];

                for (var i = tiposHorario.length - 1; i >= 0; i--) {                  
                  var coincide = true;
                  var horasAcumuladas = 0;

                  for (var j = 0; j < 5; j++) {

                    if(tiposHorario[i].horario[j] != arrMateriasAgregadas[j] && arrMateriasAgregadas[j]!=""){
                      coincide = false;
                      break;
                    }

                    var minutosClase = tiposHorario[i].horario[j].split("-")[1];
                    if(minutosClase != "null")
                      horasAcumuladas+= parseInt(minutosClase)/60;
                      
                  }

                  if(coincide && (horasXSemana == horasAcumuladas))          
                    coincidentes.push(tiposHorario[i])                    
                }

                $horarios.find("div:not([data-id-materia])").replaceWith("<div></div>");

                var horariosMateria = [];

                for (var i = coincidentes.length - 1; i >= 0; i--) {

                  horariosMateria.push(coincidentes[i].id);

                  for (var j = 0; j < 5; j++) {
                    
                    var hora = coincidentes[i].horario[j].split("-")[0]
                    $horarios.filter("[data-hora-inicio=\""+hora+"\"]").find("td:nth-child("+(j+2)+") > div:not([data-id-materia])").attr("class","target")
                      
                  }                 
                  
                };
                

                 prepareTargets($horarios.find(".target"));            
                

                return horariosMateria;               
                
              }

            });


            if($(this).data("view") != "situacionAcademica")
                return false;

            $.get("/alumnos/situacionAcademica/",function  (html) {
               $(".rightPane").html(html);

                $.getJSON("/alumnos/situacionAcademica/progresoGeneral/",function  (materias) {

                    
                    var ulMaterias = [];
                    var liMateriasSemestreA = [];
                    var liMateriasSemestreB = [];
                    var nivel = null;                    
                    var nivelAnterior = null;

                    var semestre = null;
                    
                   $.each(materias,function (key,materia) {  
                        nivel=materia.nivel; 
                        semestre =materia.semestre;

                        
                        if((nivelAnterior != nivel && nivelAnterior != null) || key == materias.length-1){

                            ulMaterias.push('<li><div class="indicadorNivel">Nivel '+nivelAnterior+'</div><ul class="listaHorizontal">'+liMateriasSemestreB.join("")+'</ul><ul class="listaHorizontal">'+liMateriasSemestreA.join("")+'</ul></li>')
                            nivel = null;
                            nivelAnterior = null;
                            
                            liMateriasSemestreA = [];
                            liMateriasSemestreB = [];
                        }

                        var dependencias = escape(JSON.stringify(materia.dependencias))
                        
                        if(semestre == 'A')
                            liMateriasSemestreA.push('<li id="mat'+materia.id+'" data-dependencias="'+dependencias+'">'+materia.nombre+'</li>')                      
                        if(semestre == 'B')
                            liMateriasSemestreB.push('<li id="mat'+materia.id+'" data-dependencias="'+dependencias+'">'+materia.nombre+'</li>')                      
                        

                        nivelAnterior = nivel;
                        
                   })       

                   $("#mapaCurricular").append(ulMaterias.join(""));


                   $("#mapaCurricular li").click(function () {

                      var dependencias = unescape($(this).attr("data-dependencias"))


                      dependencias = JSON.parse(dependencias)
                      var padre = $(this)

                      $("#mapaCurricular li").removeAttr("style")
                      padre.css({backgroundColor:'#C83F43',color:'#fff'})

                      $.each(dependencias,function (index,dependencia) {

                        var color_padre = {
                          tono:358,
                          saturacion:100,
                          luz:60
                        }    

                        var nuevo_color = 'hsl('+color_padre.tono+','+color_padre.saturacion+'%,'+(color_padre.luz+15)+'%)'
                        
                        $("#mat"+dependencia.materiaRequisito).css({backgroundColor: nuevo_color,color:'#fff' })

                        
                        if(dependencia.tipoDependencia == 'RECOMENDADO')
                          $("#mat"+dependencia.materiaRequisito).css({borderStyle: 'dotted',borderWidth: '2px',borderColor: 'hsl('+color_padre.tono+','+color_padre.saturacion+'%,'+color_padre.luz+'%)'  })
                        

                      })

                   });

                });

            });


       }
    );
});