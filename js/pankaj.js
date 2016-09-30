$(document).ready(function(){
	$(function() {
		$( "#preference" ).selectmenu();
		$( "#sortField" ).selectmenu();
	});
	$( "#reset" ).click(function(){
		$('#sortField').val(0).selectmenu('refresh',true);
		$('#preference').val(0).selectmenu('refresh',true);
		$('#sortFieldFilter').val("");
	});
	// $( "#resultTable" ).hide();
	// $( "#newSystem" ).click(function()
	// {
	// 	$(" #resultTable ").show();
	// });
});