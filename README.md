# Local Volatility Project

  From Bruno Dupire's brillant papers published during the 90's, we first aim at reproducing its work. We then hope to develop different approaches to enhance local volatility "à la Dupire" and see if and when we must adopt others tactics in order to calibrate our model, price options even the most exotic ones and hedge our positions.
  
  ## I. Classic Black Scholes reminder
  
  As a base for our work we first built a classic Black-Scholes pricer with its greeks, but its failures too ... We all know about the constant risk free rate on every maturity and even more about its constant volatility across strikes and maturities. It remains a good first step to begin our work tho.
In this objective to start with a classic Black-Scholes, we built a BlackScholes class containing closed formulas for vanilla calls and puts and for greeks computation also.

## II. Local Volatility "à la Dupire"
