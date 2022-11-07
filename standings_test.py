from connectAPI import league
from rostersMain import bloom, bannon, bshea, bnelli, rock, kcoins, feast, joe, wians, justin, jose, jackson

division1 = [rock, bannon, joe]
division2 = [jose, bloom, kcoins]
division3 = [bnelli, bshea, wians]
division4 = [feast, justin, jackson]

#box_score = league.box_scores(1)
#team1 = box_score[0].home_team
#team2 = box_score[0].away_team
#team1score = box_score[0].home_score
#team2score = box_score[0].away_score
#if team1score > team2score:
#    print("team1 wins")
#else :
#    print("team2 wins")
#we want to loop through the season


#get all games
weeks = 1
matchups = [0,1,2,3,4,5]
rockTeamDict={}
rockWins = 0
rockLoss = 0
pointFor = 0
pointAgainst = 0
divWins = 0
divLoss = 0
print("Grabbing Rock's Results....")
while weeks < 9:
    weekScore = league.box_scores(weeks)
    for y in matchups:
        homeTeam = weekScore[y].home_team
        awayTeam = weekScore[y].away_team
        homeTeamScore = weekScore[y].home_score
        awayTeamScore = weekScore[y].away_score
        if homeTeam == rock:
            pointFor = pointFor + homeTeamScore
            pointAgainst = pointAgainst + awayTeamScore
            if homeTeamScore > awayTeamScore:
                rockWins +=1
                if awayTeam == bannon or awayTeam ==joe:
                    divWins +=1
                    print(awayTeam)
            else:
                rockLoss +=1
                if awayTeam == bannon or awayTeam == joe:
                    divLoss +=1
        if awayTeam == rock:
            pointFor = pointFor + awayTeamScore
            pointAgainst = pointAgainst + homeTeamScore
            if homeTeamScore > awayTeamScore:
               rockLoss +=1
               if homeTeam == bannon or homeTeam == joe:
                   divLoss += 1
                   print(homeTeam)
            else:
                rockWins += 1
                if homeTeam == bannon or homeTeam == joe:
                    divWins += 1

    weeks+= 1
rockTeamDict.update({"wins": rockWins, "losses":rockLoss, "PointsFor":pointFor, "PointsAgainst": pointAgainst, "DivWins": divWins, "DivLosses": divLoss})
print(rockTeamDict)

#check week by week
#we need to compare home team score vs away team score, then store the winner and loser statsw
