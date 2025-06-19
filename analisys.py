import pandas as pd

# Cargar datos
df = pd.read_excel("Simulated_Power_Quality_Data.xlsx", index_col=0)

# Funciones para análisis

def check_voltage_limits(df,lim_inf = None ,lim_sup = None):
    for col in df.columns:
        if col.startswith("V_L1"):
            if lim_inf is not None :
                under_voltage = df[df[col]<lim_inf]
                print (under_voltage)
            elif lim_sup is not None:
                over_voltage = df[df[col]>lim_sup]
                print (over_voltage)
        else:
            return 0

#check_voltage_limits(df,lim_inf = 225,lim_sup=230)

            

print(df.columns)


def porcentaje_fuera_rango(df, col, limite_inf=None, limite_sup=None):
    if limite_inf is not None and limite_sup is not None:
        fuera = df[(df[col] < limite_inf) | (df[col] > limite_sup)]
    elif limite_inf is not None:
        fuera = df[df[col] < limite_inf]
    elif limite_sup is not None:
        fuera = df[df[col] > limite_sup]
    else:
        return 0
    return len(fuera) / len(df) * 100

# Indicadores

pf_low_pct = porcentaje_fuera_rango(df, "PF_L1", limite_inf=0.95) + \
             porcentaje_fuera_rango(df, "PF_L2", limite_inf=0.95) + \
             porcentaje_fuera_rango(df, "PF_L3", limite_inf=0.95)

