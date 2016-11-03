// Runs tests when button is pressed
function runTests(){
	$('#testButton').prop('disabled', true);

	window.href=
	$.get(
		"/tests/run",
		function(data) {
			$("#test-div").show();
			data = data.replace(/(ok )/g, 'ok\n')
			$("#test-output").append("<p>" + data + "</p>");
			window.dispatchEvent(new Event('resize'));
			$("#test-output").append("<button class='btn' onclick='clearTests()'>DONE</button>");
		});
}

function clearTests(){
	$("#test-div").hide();
	window.dispatchEvent(new Event('resize'));	
	$("#test-output").empty();
	$('#testButton').prop('disabled', false);
}