//Cargar información de las auditorías digitadas en el Módulo de auditorias
selectIdAudit=document.getElementById("selectIdAudit")
selectIdAudit.addEventListener("change",event=>{
    var idAuditValue= $("#selectIdAudit").val();
    

    $.ajax({
        url:'/listAudit/?buscar='+idAuditValue+'&type=idAudit',
        type:"get",
        dataType:"json",
        success:function(response){
            console.log(response);
            $("#typeAudit").text(response['typeAudit'])
            $("#auditor").text(response['auditor'])
            $("#zone").text(response['zone'])
            $("#state").text(response['state'])
            $("#city").text(response['city'])
            $("#codeAudit").text(response['codeAudit'])
            $("#ambient").text(response['ambient'])
            $("#ambientDetail").text(response['ambientDetail'])
            $("#datePlan").text(response['datePlan'])
            $("#actDetail").text(response['actDetail'])
            
        }, 
        error: function(error){
            console.log("Hay un Pendejo error")
            console.log(error);
            
        }
    }); 

});
