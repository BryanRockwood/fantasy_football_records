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
everyone = [bloom, bannon, bshea, bnelli, rock, kcoins, feast, joe, wians, justin, jose, jackson]
season = [1, 2, 3, 4, 5, 6, 7, 8]
matchups = [0,1,2,3,4,5]
zDict ={}
for z in everyone:
    zwins = 0
    zloss = 0
    zdivw = 0
    zdivl = 0
    pointFor = 0
    pointAgainst = 0
    divWins = 0
    divLoss = 0
    for x in season:
        week = league.box_scores(x)

        for y in matchups:
            ht = week[y].home_team
            at = week[y].away_team
            hts = week[y].home_score
            ats = week[y].away_score
#go through each match up, and check if its a divisional game
            if ht == z:
                pointFor = pointFor + hts
                pointAgainst = pointAgainst + ats
                if hts > ats:
                    zwins += 1
                    if ht in division1 and at in division1:
                        zdivw += 1
                    if ht in division2 and at in division2:
                        zdivw
                    if ht in division3 and at in division3:
                        zdivw += 1
                    if ht in division4 and at in division4:
                        zdivw +=1
                else:
                    zloss += 1
                    if ht in division1 and at in division1:
                        zdivl += 1
                    if ht in division2 and at in division2:
                        zdivl += 1
                    if ht in division3 and at in division3:
                        zdivl += 1
                    if ht in division4 and at in division4:
                        zdivl +=1

            if at == z:
                pointFor = pointFor + ats
                pointAgainst = pointAgainst + hts
                if hts > ats:
                    zloss += 1
                    if ht in division1 and at in division1:
                        zdivl += 1
                    if ht in division2 and at in division2:
                        zdivl += 1
                    if ht in division3 and at in division3:
                        zdivl += 1
                    if ht in division4 and at in division4:
                        zdivl += 1
                else:
                    zwins += 1
                    if ht in division1 and at in division1:
                        zdivw += 1
                    if ht in division2 and at in division2:
                        zdivw += 1
                    if ht in division3 and at in division3:
                        zdivw += 1
                    if ht in division4 and at in division4:
                        zdivw += 1

    zDict.update(
        {"wins": zwins, "losses": zloss, "PointsFor": pointFor, "PointsAgainst": pointAgainst, "DivWins": zdivw,
         "DivLosses": zdivl})
    print(z, zDict)



