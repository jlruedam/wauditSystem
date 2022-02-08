seletectedCodeAudit=document.getElementById("codeAudit")
pAudit=document.getElementById("nameAudit")
pActivities=document.getElementById("activities")

seletectedCodeAudit.addEventListener("change",event=>{

    var codeAuditValue= $("#codeAudit").val();
    console.log("El valor tomado es:")
    console.log(codeAuditValue)
       
    $.ajax({
        url:'/listUniverse/?buscar='+codeAuditValue+'&type=code',
        type:"get",
        dataType:"json",
        success:function(response){
            console.log(response.audit)
            pAudit.innerHTML=response.audit
            pActivities.innerHTML=response.activities
        }, 
        error: function(error){
            console.log("Hay un Pendejo error")
            console.log(error);
            
        }
    }); 

});
