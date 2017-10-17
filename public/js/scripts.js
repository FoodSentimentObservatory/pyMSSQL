		// function to add new field for keyword selection		
			$(function()
			{
			    $(document).on('click', '.btn-addSelection', function(e)
			    {
			        e.preventDefault();

			        var controlForm = $('.keywordGroup:first'),
			            currentEntry = $(this).parents('.entry:first'),
			            newEntry = $(currentEntry.clone()).appendTo(controlForm);

			        newEntry.find('input').val('');
			        controlForm.find('.entry:not(:last) .btn-addSelection')
			            .removeClass('btn-addSelection').addClass('btn-remove')
			            .removeClass('btn-success').addClass('btn-danger')
			            .html('<span class="glyphicon glyphicon-minus"></span>');
			    }).on('click', '.btn-remove', function(e)
			    {
					$(this).parents('.entry:first').remove();

					e.preventDefault();
					return false;
				});
			});
		//function to generate the keyword group div once the keywords have been submited
		// only allows input that contains letters, full stops and dashes
		//if no words have been added to a group and the user still tries to submit the group, an error message occurs	
			function postKeywords(){
				var keyword = document.getElementsByName("kgroups")
				var div = document.createElement("div");
					div.style.width = "100%";					
					div.style.background = "white";
					div.style.color = "black";
					div.style.border = "1px solid #E6E6FA";
					div.style.borderRadius = "10px";
					div.style.padding = "1em";
					div.style.marginBottom = "1em";
				var letters = /^[A-Za-z.-]+$/;
				document.getElementById("check").value = "some groups";
				document.getElementById("errorArea").innerHTML = ""
				if (keyword[0].value.length>0){
				var searchString=''
				layout = '<div id="closeButton"><button type="button" class="close" aria-label="Close">\
 					<span aria-hidden="true">&times;</span></button></div><div class="btn-group" data-toggle="buttons">'
 				keywordLayout =""	
				for (let i=0; i<keyword.length; i++){
					if (keyword[i].value.length>0 ){
						if (keyword[i].value.match(letters)){
							keywordLayout+="<label class='btn btn-success active space'><input type='checkbox' name='groups' checked value="+keyword[i].value+">"+ keyword[i].value+"</label>";						
							searchString +=keyword[i].value;
							if (i<keyword.length-1){
								searchString+=",";
							} 

						} else {
							keywordLayout = "<div class='alert alert-danger' role='alert'>Please, use only alphabetical characters, '.' or '-'</div>";
							document.getElementById("check").value = "no groups";	
							break;
						}		
					}
				}
				console.log(document.getElementById("check").value);
				layout = layout + keywordLayout + "<input type='hidden' name='group' value="+searchString+"></div>"
				div.innerHTML = layout;


				document.getElementById("errorMessageArea").innerHTML = "";
				document.getElementById("keywordGroupShow").appendChild(div);
			}else{
				alertMessageDiv= "<div class='alert alert-danger' role='alert'><strong>Oh snap!</strong> You must give at least one word.</div>"
		        document.getElementById("errorMessageArea").innerHTML = alertMessageDiv;
		        return false;
			}
				
			};
			// for the close button on each group bubble
			$('#keywordGroupShow').on('click', '.close', function(events){
			   $(this).parents('div').eq(1).remove();
			   document.getElementById("check").value="no groups";
			});
		//checks if every section of the homepage form has a value	
		function validateForm()	{
			var x = document.forms["searchSpecs"]["inputTypes"].value;
			var y = document.forms["searchSpecs"]["inputLocation"].value;
			var z = document.forms["searchSpecs"]["terms"].value;
		    if (x == "") {
		    	alertMessageDiv= "<div class='alert alert-danger' role='alert'><strong>Oh snap!</strong> You must select a search type</div>"
		        document.getElementById("searchTypes").innerHTML = alertMessageDiv;
		        return false;
		    } else if (y == ""){
		    	alertMessageDiv= "<div class='alert alert-danger' role='alert'><strong>Oh snap!</strong> You must select a location</div>"
		        document.getElementById("locations").innerHTML = alertMessageDiv;
		        return false;
		    } else if (z==""){
		    	alertMessageDiv= "<div class='alert alert-danger' role='alert'><strong>Oh snap!</strong> You must select a discourse</div>"
		        document.getElementById("discourses").innerHTML = alertMessageDiv;
		        return false;
		    }
		};
		//checking if there are any groups specified, if not, throw an error
		function checkForGroups() {
			var groups = document.forms["keywordGroupForm"]["check"].value;
			console.log(groups);

			if (groups == "no groups"){
				alertMessageDiv= "<div class='alert alert-danger' role='alert'><strong>Oh snap!</strong> You forgot to actually add any keyword groups :( </div>"
		        document.getElementById("errorArea").innerHTML = alertMessageDiv;
		        return false;
			}else {
				document.getElementById("check").value="no groups";
				document.getElementById("errorArea").innerHTML = "";
				$(".se-pre-con").show();
            	$("#mainContainer").hide(); 
			} 
		};
		//clear words from modal
		$('#kGroupModal').on('hidden.bs.modal', function () {
		    $(this)
				.find("input,textarea,select")
				.val('')
				.end()
		});
		//loading gif for each page
		$(window).load(function() {
		// Animate loader off screen
		$(".se-pre-con").fadeOut("slow");;
	});

		