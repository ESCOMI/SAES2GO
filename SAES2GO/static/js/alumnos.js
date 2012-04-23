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


    $("#dvNav ul li").click(
       function()
       {                    
            $.get("/alumnos/"+$(this).data("view")+"/",function  (html) {
               $(".rightPane").html(html);
            });


            $.get("/alumnos/materias/",function  (materias) {

                materias = JSON.parse(materias);
                var ulMaterias = [];
               $.each(materias,function (key) {

                   ulMaterias.push("<li>"+materias[key].fields.matNombre+"</li>")
               })       

               $("#tiraMaterias").append(ulMaterias.join(""));
            });
       }
    );
});