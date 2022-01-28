
selectedResponsable=document.getElementById("selectResponsable");
selectMacroprocess=document.getElementById("selectMacroprocess");
selectProcess=document.getElementById("selectProcess")

selectedResponsable.addEventListener("change",event=>{

    var responsable= $("#selectResponsable").val();
    
    $.ajax({
        url:'/listProcessUniverse/?buscar='+responsable+'&type=responsable',
        type:"get",
        dataType:"json",
        success:function(response){
            $('#selectMacroprocess').empty();
            $("#selectMacroprocess").append("<option value=''>...</option>");
            array_list=response.dataMacroProcess
            array_list.forEach(element => {
                console.log(element );
                $("#selectMacroprocess").append("<option value=\""+element+"\">"+element+"</option>");
            });
        }, 
        error: function(error){
            console.log(error);
        }
    }); 

});


selectMacroprocess.addEventListener("change",event=>{

    var macroprocess= $("#selectMacroprocess").val();
    
    $.ajax({
        url:'/listProcessUniverse/?buscar='+macroprocess+'&type=macroprocess',
        type:"get",
        dataType:"json",
        success:function(response){
            $('#selectProcess').empty();
            $("#selectProcess").append("<option value=''>...</option>");
            array_list=response.dataProcess
            array_list.forEach(element => {
                console.log(element );
                $("#selectProcess").append("<option value=\""+element+"\">"+element+"</option>");
            });
        }, 
        error: function(error){
            console.log(error);
        }
    }); 



});





