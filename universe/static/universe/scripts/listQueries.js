
selectedResponsable=document.getElementById("selectResponsable");
selectMacroprocess=document.getElementById("selectMacroprocess");
selectProcess=document.getElementById("selectProcess")
createCodeAudit=document.getElementById("codeAuditUniverse")


// Solicitar macroprocesos teniendo en cuenta el responsable seleccionado
selectedResponsable.addEventListener("change",event=>{

    var responsableValue= $("#selectResponsable").val();
    responsableValue=responsableValue.split(":");
    codeResponsable=responsableValue[0];
    responsable=responsableValue[1];
   
    
    $.ajax({
        url:'/listProcessUniverse/?buscar='+responsable+'&type=responsable',
        type:"get",
        dataType:"json",
        success:function(response){
            $('#selectMacroprocess').empty();
            $("#selectMacroprocess").append("<option value=''>...</option>");
            array_list=response.dataMacroProcess
            array_list.forEach(element => {
                console.log(element);
                $("#selectMacroprocess").append("<option value=\""+element+"\">"+element+"</option>");
            });
        }, 
        error: function(error){
            console.log(error);
        }
    }); 

});

// Solicitar processo teniendo en cuenta el macroproceso seleccionado
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
                
                element=element.split("/")
                console.log(element );
                $("#selectProcess").append("<option value=\""+element[0]+"\">"+element[1]+"</option>");
            });
        }, 
        error: function(error){
            console.log(error);
        }
    }); 



});

//Utilizado para crear el código de la auditoría utilizando los datos de cada lista
createCodeAudit.addEventListener("click",event=>{
    codeAuditUniverse.value="";
    // var manage=$("#selectReponsable").val();
    manage=selectedResponsable.value;
    manage=manage.split(":");
    
    var process= $("#selectProcess").val();
    var numAuditUniverse=$("#numAuditUniverse").val();
        if (numAuditUniverse.length==1){numAuditUniverse="0"+numAuditUniverse}
        if (process.length==1){process="0"+process}
    codeAuditUniverse.value=manage[0]+"-"+process+"-"+numAuditUniverse;
    
});




