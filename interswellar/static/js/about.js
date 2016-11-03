// Runs tests when button is pressed
function runTests(){
	window.href=
	$.get(
		"/tests/run",
		function(data) {
			$("#test-div").show();
			data = data.replace(/(ok )/g, 'ok\n')
			$("#test-output").append("<p>" + data + "</p>");
			$(window).trigger('resize.px.parallax');
			$("#test-output").append("<button class='btn' onclick='clearTests()'>DONE</button>");
		});
}

function clearTests(){
	$("#test-div").hide();
	$("#test-output").empty();
}