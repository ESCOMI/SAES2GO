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
       }
    );

});