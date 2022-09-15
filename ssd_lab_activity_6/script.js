let buffer = [];
function clearbuff()
{
    buffer=[];
}
function meow() {
    alert("In meow function");
let Mname = document.getElementById("Mname").value;
let Gmail = document.getElementById("Gmail").value;
let Sname = document.getElementById("Sname").value;
let Spass = document.getElementById("Spass").value;
let Cpass = document.getElementById("Cpass").value;
let Tlead = document.getElementById("Tlead").value;

    alert("Data: " + Mname + " Gmail "+ Gmail);

}
function passcheck()
{
    let in1=document.getElementById("Spass").value;
    let in2=document.getElementById("Cpass").value;
    // alert(in1+" "+ in2);
    if(in1==in2)
    {
        return 1;
    }
    else
    {
        alert("The passwords should be same");
        return 0;
    }
}
function key()
{
    
    const key = event.key;
    buffer.push(key);
    alert(buffer);
    console.log(buffer);
}
function myFunction() {
    var element = document.body;
    element.classList.toggle("light-mode");
}
function KeyPress(e) {
    var evtobj = window.event? event : e
    if (evtobj.keyCode == 77 && evtobj.ctrlKey)
        this.onclick=myFunction(); ;
}
document.onkeydown = KeyPress;
