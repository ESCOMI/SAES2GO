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

    $("#dvNav ul li").click(
       function()
       {                    
            $.get("/alumnos/"+$(this).data("view")+"/",function  (html) {

              $(".rightPane").html(html);


              $targetsMateria = $("#dvHorarios").find("table > tbody > tr > td > div");


              $targetsMateria.click(function () {

                if($materiaClonada != null){
                  $(this).attr("class","elegida").html($materiaClonada.html());
                  $materiaClonada = null;
                }

              }).dblclick(function () {
                
                  $(this).html('').attr("class","target");

              });

              // Se consultan las materias filtrando por nivel
              $("#cmbNiveles").change(function (){                  

                if($(this).val() == -1) return false;
                
                $.getJSON("/materias/",{nivel:$(this).val()},function  (materias) {

                 
                  var arrayMaterias = [];

                  $.each(materias,function (index, materia) {
                    
                    arrayMaterias.push("<li data-nivel=\""+materia.id+"\">"+materia.nombre+"</li>")

                  });

                  $("#tiraMaterias").empty().append(arrayMaterias.join("")).find("li").click(function () {
                      
                      $(this).siblings().css({backgroundColor:'#333'})  
                      $(this).css({backgroundColor:'hsl(212,100%,50%)'})
                      $materiaClonada =  $(this).clone();                      
                      $targetsMateria.not(".elegida").attr("class","target");

                  });

                });

              });


               //Se consultan los grupos
              $.getJSON("/grupos/",function  (grupos) {

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
                      padre.css({backgroundColor:'hsl(212,100%,50%)'})

                      $.each(dependencias,function (index,dependencia) {

                        var color_padre = {
                          tono:212,
                          saturacion:100,
                          luz:50
                        }    

                        var nuevo_color = 'hsl('+color_padre.tono+','+color_padre.saturacion+'%,'+(color_padre.luz+25)+'%)'
                        
                        $("#mat"+dependencia.materiaRequisito).css({backgroundColor: nuevo_color })

                        
                        if(dependencia.tipoDependencia == 'RECOMENDADO')
                          $("#mat"+dependencia.materiaRequisito).css({borderStyle: 'dotted',borderWidth: '2px',borderColor: 'hsl('+color_padre.tono+','+color_padre.saturacion+'%,'+color_padre.luz+'%)'  })
                        

                      })

                   });

                });

            });


       }
    );
});