[SedimentFileInformation]
   FileCreatedBy    = Delft3D FLOW-GUI, Version: 3.59.01.57433         
   FileCreationDate = Thu Aug 14 2025, 16:04:32         
   FileVersion      = 02.00                        
[SedimentOverall]
   Cref             =  1.6000000e+003      [kg/m3]  CSoil Reference density for hindered settling calculations
   IopSus           = 0                             If Iopsus = 1: susp. sediment size depends on local flow and wave conditions
[Sediment]
   Name             = #Sedimentsisal#               Name of sediment fraction
   SedTyp           = sand                          Must be "sand", "mud" or "bedload"
   RhoSol           =  2.7000000e+003      [kg/m3]  Specific density
   SedDia           =  3.4300000e-004      [m]      Median sediment diameter (D50)
   CDryB            =  1.6000000e+003      [kg/m3]  Dry bed density
   IniSedThick      = #capa_sed1.sdb#      [m]      Initial sediment layer thickness at bed (uniform value or filename)
   FacDSS           =  1.0000000e+000      [-]      FacDss * SedDia = Initial suspended sediment diameter. Range [0.6 - 1.0]
