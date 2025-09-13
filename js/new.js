function addmarks()
{
   // let mark1 =Number(document.getElementById("mark1").value)
     let mark1 =Number(document.getElementsByName("mark1").value)
     let mark2 =Number(document.getElementById("mark2").value)
     var total_marks=mark1+mark2
     console.log(total_marks)
     document.getElementById("result").innerHTML=total_marks
}