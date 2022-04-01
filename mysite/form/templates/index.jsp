
<%@ page import="java.io.*" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>PRM Switzerland - Compendium Webcrawler</title>
<link rel="stylesheet"
    href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script
    src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script
    src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<script>
    $(document).ready(   
    function() {    	
        function bs_input_file() {          
        	$("#downloadFrm").hide();       
            $(".input-file").before(
                function() {
                	
                    if ( ! $(this).prev().hasClass('input-ghost') ) {
                        var element = $("<input type='file' class='input-ghost' accept='.xls'  style='visibility:hidden; height:0'>");
                        element.attr("name",$(this).attr("name"));
                        element.change(function(){
                            element.next(element).find('input').val((element.val()).split('\\').pop());
                        });
                        $(this).find("button.btn-choose").click(function(){
                            element.click();
                            $("#downloadFrm").hide()
                        });                       
                       // $(this).find('input').css("cursor","pointer");
                       // $(this).find('input').mousedown(function() {
                    	    $('#file').css("cursor","pointer");
                    	  $('#file').mousedown(function() {
                            $(this).parents('.input-file').prev().click();
                            return false;
                        });
                        return element;
                    }
                }
            );
        }
         
        bs_input_file();
         
        $("#uploadBtn").on("click", function() {
            var url = "upload";
            var form = $("#uploadFrm")[0];
            var data = new FormData(form);
            $('html, body').css("cursor", "wait");           
            /* var data = {};
            data['key1'] = 'value1';
            data['key2'] = 'value2'; */
            $.ajax({
                type : "POST",
                encType : "multipart/form-data",
                url : url,
                cache : false,
                processData : false,
                contentType : false,
                data : data,
                success : function(msg) {
                	$('html, body').css("cursor", "default");
                    if (msg.status == 1) {
                    	$("#downloadFrm").show();
                    	$("#downloadFrm").attr("href","\download?path=" + msg.ouputFilePath)  
                    } else {
                        alert("Couldn't upload file");
                    }
                },
                error : function(msg) {
                	$('html, body').css("cursor", "default");
                    alert("Error processing data");
                }
            });
        }); 
        
        $("#change-pwd").on("click", function() {
        	var password =  $("#pwd").val();
        	alert (password);
        	$.post('updatePwd', { pwd: password},         			
        		function(returnedData){
        			alert("Password Updated Succesfully");
        		}).fail(function(){
        			alert("Error Updating Password");
        		});      	       
        })
        
        
        /* 
        $("#change-pwd").on("click", function() {    
  	 		alert('Change Password');
           	var url = "upload";
           	$.ajax({
                   type : "GET",
                   dataType : "text",
                   url : url,
                   cache : false,
                   data : $("#pwd").value,
                   contentType : false,
                   success : function(msg) {  
                   	alert("Password Updated Succesfully");                  	                    
                   },
                   error : function(fcc) {
                   	alert("Error Updating Password");       
                   }
               });              
    
        });
       
       
        $("#downloadButton").on("click", function() {
            var url = "download";
            var form = $("#uploadFrm")[0];
            var data = new FormData(form);
             var data = {};
            data['path'] = $("#ouputFilePath").attr("value");            
            $.ajax({
                type : "POST",
                encType : "application/json",
                datatype : "json",
                url : url,
                cache : false,
                processData : false,
                contentType : false,
                data : data,
                success : function(msg) {
                	 alert("upload file");      
                },
                error : function(msg) {
                    alert("Couldn't upload file");
                }
            });
        }); */
    });
</script>
</head>

<body>

	<div class="container" id="container1">
		<img src="img/IQ_LOGO.png" alt="IQVIA" style="width: 200px">
		<div class="col-md-8 col-md-offset-2">
			<h3>PRM Swiss - Compendium Webcrawler</h3>
			<form id="uploadFrm" method="POST" action="#" 
				enctype="multipart/form-data">
				<!-- COMPONENT START -->
				<div class="form-group">
					<div class="input-group input-file" name="file">
						<span class="input-group-btn">
							<button class="btn btn-default btn-choose" type="button">Choose</button>
						</span> <input type="text" class="form-control" id="file" name="file"
							placeholder='Choose products .xls file...' /> <span
							class="input-group-btn"> <input type="hidden"
							name="dummyIEField" value=""> <!--  credentials -->
							<button type="button" class="btn btn-primary pull-right"
								id="uploadBtn">Submit</button>
						</span>
					</div>
				</div>
				<a id="downloadFrm" href="" class="btn btn-primary btn-lg btn-block">Download
					results file</a>
			</form>

			<!-- 			<form id="downloadFrm" method="POST" action="#" -->
			<!-- 				enctype="multipart/form-data">	 -->
			<!-- 				<input id="ouputFilePath" type="hidden" value="">			 -->
			<!-- 				<button type="button" class="btn btn-primary btn-lg btn-block" id="downloadButton"> -->
			<!-- 					Download results file -->
			<!-- 				</button> -->
			<!-- 			</form> -->
		</div>
	</div>
	<br>
	<div class="container" id="container2">
		<div class="col-md-8 col-md-offset-2" align="right">
			<form id="change-pwd-form" class="form-inline" method="POST" action="#">			
				<div class="form-group">
				<div class="input-group input-file">
					<span class="input-group-btn">
						<input type="text" class="form-control" name="pwd" id="pwd"
							placeholder="New Password">
				</span>
					<span class="input-group-btn">
					 <input
							type="hidden" name="dummyIEField2" value="test">
						<button type="submit" class="btn btn-primary" id="change-pwd">
							Update Password
						</button>
					</span>
				</div>
				</div>
			</form>
		</div>
	</div>
	
</body>
</html>
