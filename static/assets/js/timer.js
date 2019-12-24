 // Get today's date and time
 var now = new Date().getTime();
         
 // Find the distance between now and the count down date    
 //var distance = countDownDate - now;
var countDownDate= Date.parse('30 OCT 2019 00:00:00 GMT');
function time_diff(now,countDownDate){
    var x = setInterval(function() {

       
        var distance=countDownDate-now
        // console.log(countDownDate)
        // console.log(now)
        // console.log(distance)
        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
          
        // Output the result in an element with id="demo"
      
        document.getElementById("days").innerHTML = days
        document.getElementById("hours").innerHTML = hours
        document.getElementById("minutes").innerHTML = minutes
        document.getElementById("seconds").innerHTML = seconds
        // If the count down is over, write some text 
        if (distance < 0) {
          clearInterval(x);
          document.getElementById("timing").innerHTML = "<h1 >Expired</h1>";
        }
      }, 0)
}

time_diff(now,countDownDate)