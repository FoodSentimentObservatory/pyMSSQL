var availableTags = [];
function getKeywords(){
	var keywordString = localStorage['objectToPass'];
	var listOfKeywords = keywordString.split("; ")
	for (i=0;i<listOfKeywords.length;i++){
		availableTags.push(listOfKeywords[i]);
	}
	console.log(listOfKeywords);
}					    
// function to add new field for keyword selection	
	$(function(){
			    $(document).on('click', '.btn-addSelection', function(e) {		    	 
			        e.preventDefault();

			        var controlForm = $('.keywordGroup:first'),
			            currentEntry = $(this).parents('.entry:first'),
			            newEntry = $(currentEntry.clone()).appendTo(controlForm);
			        //section to add autocomplete to the newly generated fields . 
			        //only matches to tags with the same starting letter   

			        $(".keywordGroup").find('input[type=text]:last').autocomplete({

			                source: function( request, response ) {
						          var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( request.term ), "i" );
						          response( $.grep( availableTags, function( item ){
						              return matcher.test( item );
						          }) );
						      }
			            });

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
				var letters = /^[A-Za-z.-\s]+$/;
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
			var y = document.forms["searchSpecs"]["searchnoteID"].value;
			
		    if (x == "") {
		    	alertMessageDiv= "<div class='alert alert-danger' role='alert'><strong>Oh snap!</strong> You must select a search type</div>"
		        document.getElementById("searchTypes").innerHTML = alertMessageDiv;
		        return false;
		    } else if (y == ""){
		    	alertMessageDiv= "<div class='alert alert-danger' role='alert'><strong>Oh snap!</strong> You must select a search definition.</div>"
		        document.getElementById("searchDefs").innerHTML = alertMessageDiv;
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

	function setDb(dbName){
		document.getElementById("dbName").value = dbName;
		console.log(document.getElementById("dbName").value);
	}	
	//function to display information on click of each search button
	function displaySearchData(searchName,earliest,latest,keywordString, total, coordinates){
		//processing the coordinates from string python list to a json array
		var coordinatesList = [];
		coordinateListS = coordinates.split('], [')
		for (i = 0; i<coordinateListS.length; i++){
			coorList = coordinateListS[i].split('), (');
			coordinatesList.push(coorList);
		}
		var properCoordinatersList= [];
		for (i = 0; i<coordinatesList.length; i++){	
			for (n=0; n<coordinatesList[i].length;n++){
				listOfCoorForSearch = coordinatesList[i][n].split(', ');
				var searchCoorsList = [];
				for (z=0;z<listOfCoorForSearch.length;z++){
					var coorstr = listOfCoorForSearch[z].replace(/[[\]()]/g,'');
					var coorint = parseFloat(coorstr);
					searchCoorsList.push(coorint);
				}
				properCoordinatersList.push(searchCoorsList);
			}
		}
		var pointList=[]
		for (n=0;n<properCoordinatersList.length;n++){
			var point= new Coordinates(properCoordinatersList[n]);
			pointList.push(point);
		}

		var jsonPointListStr=JSON.stringify(pointList);
		var jsonPointList = JSON.parse(jsonPointListStr);
		//creating the map with the relevant coordinates
		initMap(jsonPointList);

		document.getElementById("start").value = earliest;
		document.getElementById("endof").value = latest;
		//generating a div with the search info
		layout = "<div id='info'><h4>"+searchName+"</h4><strong>Total of tweets in this search: </strong>"+total+"</br><strong>Oldest tweet available published on:</strong> "+earliest+"</br><strong>Most recent tweet available published on:</strong> "+latest+"</br><strong>Keywords and phrases of the search:</strong><br> "+keywordString+"</div>";

		document.getElementById("searchData").innerHTML=layout;	
	};	
	//function to create a json array for each point
	function Coordinates(coordinatesData){
		this.rad=coordinatesData[0];
		this.center={};
		this.center["lat"]=coordinatesData[1];
		this.center["lng"]=coordinatesData[2];
	}

 function initMap(jsonPointList) {
 
        // Create the map.
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: {lat: 54.695002, lng: -2.658691},
          mapTypeId: 'terrain'
        });
        // Construct the circle for each value in the point list.
        // Note: the radius is measured in meters so we need to multply it by 1000
        for (var city in jsonPointList) {
          // Add the circle for this city to the map.
          var cityCircle = new google.maps.Circle({
            strokeColor: '#FF0000',
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: '#FF0000',
            fillOpacity: 0.35,
            map: map,
            center: jsonPointList[city].center,
            radius: 1000*jsonPointList[city].rad
          });
        }
      };
//function to initialize the date picker with start and end date of the selected search
 $(function(){	
 	$('.input-daterange input').datetimepicker({
 		autoclose:true,
 		format:'YYYY-MM-DD HH:mm',
 		minDate: new Date(document.getElementById("fromDate").value),
	    maxDate: new Date(document.getElementById("toDate").value),
 	})

 });

	   $("input[name='kgroups']").autocomplete({

  		source: function( request, response ) {

          var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( request.term ), "i" );
          response( $.grep( availableTags, function( item ){
              return matcher.test( item );
          }) );
      }
});
