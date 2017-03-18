# ONLINE APPENDIX: Growth in a Time of Austerity: Evidence from the UK
Juergen Amann and Paul Middleditch  




This document reproduces the empirical findings in @AM2016.


# Data 

Some data manipulations are required to derive the monthly data series used in @AM2016. Below, we discuss these calculations and provide visual evidence of the legitimacy of all steps undertaken.

## Gross Government Debt (DoG)


### Raw Data
Quarterly data on gross government debt is readily available (e.g *‘quarterly government debt’* from Eurostat and *‘general government total gross debt’* from the OECDStats.StatExtracts). [^longnote1] However, only United Kingdom Office of National Statistics (UK-ONS) offers *'Public Sector Net Debt'* (PSND from now on) on a monthly basis.[^longnote2]



Below we plot all these three series as well as the (annual) RR 2010 data set against time.

![](OnlineAppendix_files/figure-html/unnamed-chunk-2-1.png)<!-- -->

### Data Manipulation

Following data availability issues we describe the construction of a series for monthly gross debt for the UK, showing the data manipulations undertaken.  

As quarterly gross debt and quarterly PSND data are freely available, we begin by comparing both series with each other. Note the similar and parallel nature of both series in the plot below.

![](OnlineAppendix_files/figure-html/unnamed-chunk-3-1.png)<!-- -->


This observation is generally confirmed in the figure below where we plot the difference, in percent points, of both series against time (black line). By inspection we can see that, through the crisis, the difference between gross debt and PNSD has increased. Given the data structure as shown below, this series was then disaggregated from quarterly to monthly data using R's `tempdisagg` package using the Denton-Cholette method (red line in graph below).

![](OnlineAppendix_files/figure-html/unnamed-chunk-4-1.png)<!-- -->

In a next step, we add the disaggregated difference, plotted above (red line), to the monthly PSND series and present in the graph below (cyan line).



![](OnlineAppendix_files/figure-html/unnamed-chunk-5-1.png)<!-- -->

Furthermore we note that this newly derived series appears to display a strong seasonal pattern which we remove in the subsequent step. For this we use "Census X-13", the Seasonal Adjustment Program developed by the United States Census Bureau for this purpose through the R interface `seasonal`.[^longnote3]



The next figure confirms that the strong seasonal pattern could be removed, thereby producing a smooth(er) series. 

![](OnlineAppendix_files/figure-html/unnamed-chunk-6-1.png)<!-- -->

Finally the plot below compares the newly derived monthly DoG series against OECD and Eurostat data.

![](OnlineAppendix_files/figure-html/unnamed-chunk-7-1.png)<!-- -->



## GDP Growth Rates (GR)

### Raw Data

For monthly GDP growth rates, we make use of monthly estimates from the *National Institute of Economic and Social Research* (NIESR). This series was estimated following the methodology described in [@NIESR], expressed as an index where 2008 = 100. We present the NIESR series below:

![](OnlineAppendix_files/figure-html/unnamed-chunk-8-1.png)<!-- -->

### Data Manipulation

Using these indexed GDP estimates we calculate the *percent growth rate in change over the same month of the previous year* (GR from now on). In order to compare this calculated series with other GDP measures commonly used by researchers, we plot our monthly series (cyan line) against time and vis-a-vis equivalent GDP growth rates provided by UK-ONS (green line), the OECD (black line) and the RR 2010 data (blue line).[^longnote4]




![](OnlineAppendix_files/figure-html/unnamed-chunk-9-1.png)<!-- -->

## Final Data Set

### Summary Statistics


|  |DoG | GR |
| --- |  --- |  --- |
| Min | 35.60 | -7.12 |
| Max | 89.40 | 6.13 |
| Mean | 51.12 | 2.15 |
| Median | 43.89 | 2.69 |
| SE | 11.42 | 0.16 |
| N | 216 | 216 |







### Exploratory Data Analysis

Below we reproduce Figure 1 in @AM2016. 

![](OnlineAppendix_files/figure-html/unnamed-chunk-10-1.png)<!-- -->![](OnlineAppendix_files/figure-html/unnamed-chunk-10-2.png)<!-- -->



# Footnotes

[^longnote1]: Eurostat data: The full data set including meta data can be downloaded from http://epp.urostat.ec.europa.eu/cache/ITY_SDDS/EN/gov_q_ggdebt_esms.htm. OECD.StatExtract quarterly National Accounts (Quarterly Public Sectors Debt, percent of GDP; data can
be found at http://stats.oecd.org/Index.aspx?DataSetCode=GOV_DEBT.

[^longnote2]: Available at http://www.quandl.com/UKONS/PUSF_HF6X_M-PSND-excluding-NR-as-a-of-GDP-Monthly.

[^longnote3]: Please see https://www.census.gov/srd/www/winx13/. A detailed description of the procedure is presented in the reference manual available at https://www.census.gov/ts/x13as/docX13AS.pdf. R Interface to X-13-ARIMA-SEATS: https://cran.r-project.org/web/packages/seasonal/index.html

[^longnote4]: The OECD data, *quarterly growth rates of real GDP, changes over same quarter, previous year*, is taken from http://stats.oecd.org/index.aspx?queryid=26674 . Data from UK-ONS, *gross domestic product: quarter on quarter previous year: CVM SA (Quarterly)*, is taken from http://stats.oecd.org/index.aspx?queryid=26674.

[^longnote5]:
Rapach and Wohar (2006) use the Bai Perron break point test in a very similar way as we do but don't actually test for Granger-causality (https://www.researchgate.net/profile/Mark_Wohar2/publication/5168421_Regime_Changes_in_International_Real_Interest_Rates_Are_They_a_Monetary_Phenomenon/links/54f467fd0cf299c8d9e748b0.pdf). Giacomini and Rossi (2006) write: "To address these issues and to complement the empirical results in Stock and Watson (1999) and Estrella et al. (2003), we therefore consider the test proposed by Elliott and Mueller (2003), which has optimal power against multiple structural breaks. In addition, we report results using the structural break tests of Andrews (1993), Andrews and Ploberger (1994), Nyblom (1989) and Ghysels, Guay and Hall (1997)" (http://public.econ.duke.edu/~brossi/GiacominiRossiOxfordBullettin2006.pdf). In line with the other two papers, Chen, Rogoff and Rossi (2010) also employ this testing framework on stationary data (http://public.econ.duke.edu/~brossi/ChenRogoffRossi2008.pdf).  
Ajmi et al 2014: Their first empirical step is to use standard unit root tests to show stationarity, then employ a Granger-causality test and then discuss structural stability. (http://www.ipag.fr/wp-content/uploads/recherche/WP/IPAG_WP_2014_296.pdf).
**NOTE FOR PAPER: Maybe we want to extend this literature list a bit more.**

[^longnote6]:
Titus Awokuse (2002) also run a Toda Yamamoto Granger-causality on the full sample, then test for previous assumed break points using a Chow test, find evidence for a break and re-run the test for the sub sample (http://ageconsearch.umn.edu/bitstream/15823/1/sp020001.pdf). More closely related is the study by Stern and Enflo (2013) who also use unit root tests to define endogenously found break dates that are then introduced into the VAR system. They also use the TY procedure for their subsequent analysis but do not the issue of parameter stability as extensively as we do here (http://faculty.smu.edu/millimet/classes/eco6375/papers/stern%20enflo%202013.pdf).


[^longnote7]: We conduct these tests in R and make use use of the package *strucchange*. For more information please see http://eeecon.uibk.ac.at/~zeileis/papers/Zeileis+Kleiber+Kraemer-2003.pdf and https://cran.r-project.org/web/packages/strucchange/vignettes/strucchange-intro.pdf.
