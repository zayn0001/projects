document.querySelector("#eventtype1").onclick = function() {  
    document.querySelector("#eventstarttime").value = '00:00';
    document.querySelector("#eventendtime").value = '23:59';
    $("#eventstarttime").prop('readonly', true);
    $("#eventendtime").prop('readonly', true);
}
document.querySelector("#eventtype2").onclick = function() {  
    document.querySelector("#eventstarttime").value = '';
    document.querySelector("#eventendtime").value = '';
    $("#eventstarttime").prop('readonly', false);
    $("#eventendtime").prop('readonly', false);
}

document.querySelector("#myform").addEventListener("submit",
    function(event){
        console.log("here")
        event.preventDefault();
        handleForm(this)
    }, true)

function handleForm(form){

    var missing = false
    var compulsory = ['eventname','eventimp','eventdate','eventype','eventstarttime','eventendtime','desc','recurrance','eventpurpose']
    for (i=0;i<compulsory.length;i++) {
        if (form[compulsory[i]].value == '') {
        console.log("missing parameters but defined!!" + compulsory[i]);
        missing = true
        console.log(missing)
        }
    }
    if (missing==true) {
        console.log("reached here")
        document.querySelector(".alertmsg").style.display = ""
    }
    else {
        console.log("how tf did it reach here")
        google.script.run.hello(form);
        location.replace("https://www.google.com/")
    }
}