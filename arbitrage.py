def calculate_arbitrage(bankroll, X_outcome_A, X_outcome_B, Y_outcome_A, Y_outcome_B):
    X_outcome_A_Y_Outcome_B_Arbitrage_Percent = round(100 * (1 - (X_outcome_A + Y_outcome_B)),4)

    X_outcome_B_Y_Outcome_A_Arbitrage_Percent = round(100 * (1 - (X_outcome_B + Y_outcome_A)),4)

    if (X_outcome_A_Y_Outcome_B_Arbitrage_Percent <= 0 and X_outcome_B_Y_Outcome_A_Arbitrage_Percent <= 0):
        print("No arbitrage oppertunity")
        return

    cost_X = 0
    cost_Y = 0
    shares_X = 0
    shares_Y = 0

    maximum_profit = 0
    gaurenteed_profit = 0

    optimal_cost_X = 0
    optimal_cost_Y = 0

    if (X_outcome_A_Y_Outcome_B_Arbitrage_Percent >= X_outcome_B_Y_Outcome_A_Arbitrage_Percent):
        step = 0
        while step <= bankroll:
            cost_X = step
            step += 0.01
            cost_Y = (bankroll - step)

            shares_X = round(cost_X / X_outcome_A,2)
            shares_Y = round(cost_Y / Y_outcome_B,2)

            if (shares_X >= bankroll and shares_Y >= bankroll):
                gaurenteed_profit = min(shares_X - bankroll, shares_Y - bankroll)
                if (gaurenteed_profit > maximum_profit):
                    maximum_profit = round(gaurenteed_profit,2)
                    optimal_cost_X = round(cost_X,2)
                    optimal_cost_Y = round(cost_Y,2)
            
    else:
        step = 0
        while step <= bankroll:
            cost_X = step
            step += 0.01
            cost_Y = (bankroll - step)

            shares_X = round(cost_X / X_outcome_B,2)
            shares_Y = round(cost_Y / Y_outcome_A,2)

            if (shares_X >= bankroll and shares_Y >= bankroll):
                gaurenteed_profit = min(shares_X - bankroll, shares_Y - bankroll)
                if (gaurenteed_profit > maximum_profit):
                    maximum_profit = round(gaurenteed_profit,2)
                    optimal_cost_X = round(cost_X,2)
                    optimal_cost_Y = round(cost_Y,2)

    if (X_outcome_A_Y_Outcome_B_Arbitrage_Percent >= X_outcome_B_Y_Outcome_A_Arbitrage_Percent):
        print(f"Arbitrage %: {X_outcome_A_Y_Outcome_B_Arbitrage_Percent}%   Gaurenteed profit: ${maximum_profit}    Platform X buy A: ${optimal_cost_X}   Plaform Y buy B: ${optimal_cost_Y}")
    else:
        print(f"Arbitrage %: {X_outcome_B_Y_Outcome_A_Arbitrage_Percent}%   Gaurenteed profit: ${maximum_profit}    Platform X buy B: ${optimal_cost_X}   Plaform Y buy A: ${optimal_cost_Y}")

        
calculate_arbitrage(1000, 0.63, 0.38, 0.73, 0.28); # bankroll, A(yes, no), B(yes, no)