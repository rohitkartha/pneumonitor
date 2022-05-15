
var input = document.querySelector('#upload'); 
document.getElementById("goBtn").style.display = "none";
//document.getElementById("responseField").style.display = "none";
document.getElementById("buttonload").style.display = "none";



input.addEventListener('change', function(e){



fileName = event.target.files[0] 

if(fileName== null){
    alert("nothing selected")
}
else{

    console.log(event.target.files[0].name); 

    document.querySelector(".button").innerHTML = event.target.files[0].name;


    document.getElementById("goBtn").style.display = "";

    document.getElementById("responseField").style.display = "";

    document.getElementById("goBtn").addEventListener('click', async _ => {
        document.getElementById("buttonload").style.display = "";

    });
    
}})




