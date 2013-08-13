//pulling all the custom js functionality from vb app into separate file

						var NumDoublesPlayers; //doesn't change
						var NumGroupPlayers; // original num of group players; doesn't change
						var RemainingGroupPlayers; // tracking the current number of players to place on a court
						var Num2CourtsFixed; // 2s courts from original doubles players
						var Num2CourtsGroup = 0; // 2s courts from original group players
						var TotNum2Courts;
						var Num3Courts; //min 6 people
						var Num4Courts; //min 8 people
						var ExtraPlayer;
						var arrRandomPlayers = []; //pulled out b/c used in 2 functions (not sure if better to make global vs passing it as param into 2nd fnc) 
						var arr4Teams = []; 
						var arr3Teams = [];
						var arr2Teams = [];
						var listTeams = []; //used to track which teams added to which court
						var listCourts = []; //track which courts were created

					    var win_width = $(window).width();
					    //console.log("window width: " + width);
					    var win_height = $(window).height();
					    //console.log("window height: " + height);
					    var rect_width = 105;
					    var rect_height = 135;

//custom object - team (int num, array players, int size)
						function Team(num, players) { 
						    this.num = num; //team number, tracked by var teamCount for how many teams have been created
						    this.players = players;
						    this.size = players.length;
						}
			//Team.prototype.addPlayers = function() {
			 //   return ;
			//}

//custom object - court (object teams)
						function Court(num, team1, team2) {
							this.num = num;
						    this.team1 = team1;
						    this.team2 = team2;
						    this.size = team1.size;
						    //this.size = size;
						}
						//Court.prototype.addTeams = function() {
						  //  return ;
						//}

						//numSizeCourts should be refactored and enhanced
						//break into 3-4 subfunctions
						//1 for group players, recursive functions that breaks the group into 3, then 4 player teams
						//2 for remaining group players (after goen thru #1), breaks group into 2 player team
						//3 for original 2 player teams, counts # courts (think about whether courts should be created here rather than below)
						//consider: maybe there should be one combined button: Get Courts and Teams (first goes through 4's, 3's, 2's)
						//2nd combined button: Get Courts and Teams (mostly group teams); goes through 3's and 4's and probably only 1 
						//additional 2's team

						function numSizeCourts () {  
							var ExtraMessage = "";

							NumGroupPlayers = $("#NumGroupPlayers").val(); //doesn't change
							NumDoublesPlayers = $("#NumDoublesPlayers").val(); //doesn't change
							Num2CourtsFixed = NumDoublesPlayers / 4;
							Num3Courts = 0; //min 6 people
							Num4Courts = 0; //min 8 people
							ExtraPlayer = 0;

							console.log("number doubles players: " + NumDoublesPlayers);
							console.log("number group players: " + NumGroupPlayers);

							RemainingGroupPlayers = NumGroupPlayers;

//trying to fix court num logic
							getGroupCourts(RemainingGroupPlayers);
//this always gives an undefined value; possibly b/c on the first iteration of getGroupCourts, I think there is no return
							//console.log("RemainingGroupPlayers after getGroupCourts: " + LeftoverGroupPlayers);
							//RemainingGroupPlayers = LeftoverGroupPlayers;

							if (RemainingGroupPlayers >= 4) { //added check to fix case where ending up with negative values for RemainingGroupPlayers and ExtraPlayer
								Num2CourtsGroup += 1;
								RemainingGroupPlayers -= 4;						
							}

							TotNum2Courts = Num2CourtsFixed + Num2CourtsGroup;

							if (RemainingGroupPlayers < 4) { //	4 otherwise remaining players < 4
								ExtraPlayer = ExtraPlayer + RemainingGroupPlayers;
								ExtraMessage = "There will be " + ExtraPlayer + " extra player(s) to manually assign to teams.";
							}

							//print num courts and team sizes
							$('#court_results').append('<li><h4>Court Results:</h4></li>');

							if (Num4Courts > 0) {
								$('#court_results').append('<li><p>'+Num4Courts+' court(s) for 4\'s </p></li>');
								console.log(Num4Courts + " courts for 4's");
							}
							if (Num3Courts > 0) {
								$('#court_results').append('<li><p>'+Num3Courts+' court(s) for 3\'s </p></li>');
								console.log(Num3Courts + " courts for 3's");
							}
							if (Num2CourtsFixed + Num2CourtsGroup > 0) {
								$('#court_results').append('<li><p>'+TotNum2Courts+' court(s) for 2\'s </p></li>');
								console.log(TotNum2Courts + " courts for 2's");
							}
							if (ExtraPlayer > 0) {
								$('#court_results').append('<li><p>'+ExtraMessage+'</p></li>');
								console.log(ExtraMessage);
							}

						} //end numSizeCourts()

//trying to fix court num logic
						function getGroupCourts(remainingPlayers) {
							if (remainingPlayers < 6) {
//issue where remainingPlayers is undefined	
//this only gets printed when I update the value of RemainingGroupPlayers (rather than remainingPlayers within the else statement)							
								console.log("remainingPlayers after recursion: " + remainingPlayers);
								return remainingPlayers;
							}
							else {
								if (remainingPlayers >= 6) { //2 check if remaining players >= 6; 3's court
									Num3Courts += 1;
//not positive whether to update remainingPlayers (param) vs RemainingGroupPlayers		
									remainingPlayers -= 6;							
									RemainingGroupPlayers -= 6;
								}
								if (remainingPlayers >= 8) { //1 check if remaining players >= 8; 4's court
									Num4Courts += 1;
									remainingPlayers -=8;
									RemainingGroupPlayers -= 8;
								}
								if (remainingPlayers >= 6) {
									getGroupCourts(RemainingGroupPlayers)
								}
							}
							console.log("remainingPlayers: " + remainingPlayers);
							console.log("RemainingGroupPlayers: " + RemainingGroupPlayers);
						}

						function randomGroupTeams () {
							//	1 create an array with a list of numbers (1 - NumGroupPlayers)
							var arrDoublesPlayers = []; 
							var arrGroupPlayers = [];
							var arrRandom2sPlayers = []

							if (NumDoublesPlayers > 0) {
								for (var i = 0; i< NumDoublesPlayers; i++) {
									arrDoublesPlayers[i] = i + 1;
								}
								console.log("length arrDoublesPlayers: " + arrDoublesPlayers.length);
								console.log("first arrayDoublesPlayers: " + arrDoublesPlayers[0]);
								console.log("last arrayDoublesPlayers: " + arrDoublesPlayers[arrDoublesPlayers.length - 1]);

								arrRandom2sPlayers = randomizeArray(arrDoublesPlayers); //only randomize list if there are known doubles players
								console.log("randomized 2s players: " + arrRandom2sPlayers);					
							}

							for (var j = 0; j < NumGroupPlayers; j++) {
								arrGroupPlayers[j] = j + Number(NumDoublesPlayers) + 1;
							}
							console.log("length arrGroupPlayers: " + arrGroupPlayers.length);
							console.log("first arrayGroupPlayers: " + arrGroupPlayers[0]);
							console.log("last arrayGroupPlayers: " + arrGroupPlayers[arrGroupPlayers.length - 1]);

							//1b put the arrGroupPlayers in a random order
							arrRandomPlayers = randomizeArray(arrGroupPlayers);	
							console.log("randomized group players: " + arrRandomPlayers);

							//assignPlayersTeams(); //issue is not sure how to get the count of 2s, 3s, 4s courts from other function
							//issue not sure how to assign the extra players? add them to largest teams first?

							var curRandomPlayer = 0;

							for (var k = 0; k < (Num4Courts * 8); k++) { //assign players to 4s courts
								var added4 = arr4Teams.push(arrRandomPlayers[k]);					
							}

							curRandomPlayer = (Num4Courts * 8);

							for (var m = 0; m < (Num3Courts * 6); m++) { //assign players to 3s courts
								var added3 = arr3Teams.push(arrRandomPlayers[curRandomPlayer + m]);
							}

							curRandomPlayer = curRandomPlayer + (Num3Courts * 6);

							for (var n = 0; n < (Num2CourtsGroup * 4); n++) { //assign group players to 2s courts
								var added2 = arr2Teams.push(arrRandomPlayers[curRandomPlayer + n]);
							}

							console.log("arr2Teams from group players: " + arr2Teams);

							curRandomPlayer = curRandomPlayer + (Num2CourtsGroup * 4);

							for (var p = 0; p < arrRandom2sPlayers.length; p++) { //assign known doubles players to 2s courts
								var added2 = arr2Teams.push(arrRandom2sPlayers[p]);
							}

							console.log("final arr2Teams: " + arr2Teams);
							assignTeams();
							assignCourts();
							displayTeamResults(); //located in the body of the app html near canvas element

						} //end randomGroupTeams()

						function randomizeArray (array1) { //not crazy about logic, would like to improve it where 1/3 of time, insert a number around the middle of the array
							var tempArray = [];
							for (var i = 0; i < array1.length; i++) { 
								var numRandom = getRandomArbitrary(0,1);
								if (Math.round(numRandom)) {
									tempArray.push(array1[i]);
								} else {
									tempArray.unshift(array1[i]);
								}
								console.log("random num: " + numRandom);
								console.log("rounded random num: " + Math.round(numRandom));
								console.log("tempArray updated for " + i + " " + tempArray);
							}
							return tempArray;
						} //end randomizeArray(array1)

						function getRandomArbitrary(min, max) {
			 				return Math.random() * (max - min) + min;
						}

						function assignTeams () { //instantiate the team objects
							//take arr4Teams and split the list of random 4s players into separate teams
							var count = 1;
							for (var i = 0; i < arr4Teams.length; i + 4) { //assigns random players to 4s teams
								var team4Players = [];
								var teamName = "team" + count; //not sure this does anything
								team4Players = arr4Teams.splice(0, 4);
								var teamName = new Team(count, team4Players);
								listTeams.push(teamName);
								count++;
								//i += 3; // for every iteration of the loop, want to increment i by 4
								console.log("Team " + teamName.num + " players: " + teamName.players + "(" + teamName.size + ")");
								console.log("arr4Teams: " + arr4Teams);
							}

							for (var i = 0; i < arr3Teams.length; i + 3) { //assigns random players to 3s teams
								var team3Players = [];
								var teamName = "team" + count; //not sure this does anything
								team3Players = arr3Teams.splice(0, 3);
								var teamName = new Team(count, team3Players);
								listTeams.push(teamName);
								count++;
								//i += 2; // for every iteration of the loop, want to increment i by 3
								console.log("Team " + teamName.num + " players: " + teamName.players + "(" + teamName.size + ")");
								console.log("arr3Teams: " + arr3Teams);
							}

							for (var i = 0; i < arr2Teams.length; i + 2) { //assigns random players to 2s teams
								var team2Players = [];
								var teamName = "team" + count; //not sure this does anything
								team2Players = arr2Teams.splice(0, 2);
								var teamName = new Team(count, team2Players);
								listTeams.push(teamName);
								count++;
								//i += 1; // for every iteration of the loop, want to increment i by 2
								console.log("Team " + teamName.num + " players: " + teamName.players + "(" + teamName.size + ")");
								console.log("arr2Teams: " + arr2Teams);
							}

							//check listTeams elements
							for (var i=0; i < listTeams.length; i++) {
								console.log("list Teams - team num: " + listTeams[i].num);
							}

							//chrome not yet supporting js v1.7; check listTeams elements
							//var item = Iterator(listTeams);
							//for (var pair in item) {
							//	console.log("listTeams: " + pair);
							//}

						}

						function assignCourts () { //instantiate the court objects
							//iterate through listTeams array
							var count2 = 1;
							for (var j=0; j < listTeams.length; j++) {
								//console.log("length listTeams: " + listTeams.length);
								var courtName = "court" + count2; //not sure this does anything
								var courtName = new Court(count2, listTeams[j], listTeams[j + 1]);
								listCourts.push(courtName);
								console.log("court" + count2);
								console.log(" team" + listTeams[j].num + " size: " + listTeams[j].size + "; players: " + listTeams[j].players);
								console.log(" team" + listTeams[j+1].num + " size: " + listTeams[j+1].size + "; players: " + listTeams[j+1].players);
								//console.log("j: " + j + "; j + 1:" + (j + 1));
								//console.log("Court " + courtName.num + " teams: " + courtName.team1.num + ", " + courtName.team2.num);
								//console.log("length listTeams: " + listTeams.length);					
								count2++;
								j += 1; //for every iteration through for loop, wanted to increment j by 2, this resolved issue
							}

							console.log("length listCourts: " + listCourts.length);
							//check listCourts elements
							//for (var i=0; i< listCourts.length; i++) {
								//console.log("list Court - Court" + listCourts[i].num);
							//}
						}
						
						//button event handlers
						$(document).ready(function() {
							$("#btnNumSizeCourt").bind("click", numSizeCourts); //event handler for btnNumSizeCourt
							$("#btnRandomGroup").bind("click", randomGroupTeams); //event handler for btnRandomGroup 
						});