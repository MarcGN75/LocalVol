# Local Volatility Project

  From Bruno Dupire's brillant papers published during the 90's, we first aim at reproducing its work. We then hope to develop different approaches to enhance local volatility "à la Dupire" and see if and when we must adopt others tactics in order to calibrate our model, price options even the most exotic ones and hedge our positions.
  
  ## I. Classic Black Scholes reminder
  
  As a base for our work we first built a classic Black-Scholes pricer with its greeks, but its failures too ... We all know about the constant risk free rate on every maturity and even more about its constant volatility across strikes and maturities. It remains a good first step to begin our work tho.
In this objective to start with a classic Black-Scholes, we built a BlackScholes class containing closed formulas for vanilla calls and puts and for greeks computation also.

## II. Local Volatility "à la Dupire"

  From a development of dupire's local volatility function found in "Local Volatility and Dupire's Equation" and first presented in Lipton (2002) and Gatheral (2006), we expect to fit the implied volatility smile with only one "smooth" enough function of the implied volatility (details ...). Building on our Black Scholes model pricing on local volatility for each couple (Strike, Maturity), we create a dupire class that would be able, with the help of the function mentionned above to find the correct market prices.
If so, this conitnuous function would give us the full underlying's distribution - not only de densities at maturity. This would be a massive help in order to price exotic derivatives like path-dependent assets.
