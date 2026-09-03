import numpy as np
import pandas as pd
rng = np.random.default_rng(42)
horas = rng.uniform(0, 10, 1000)
frequencia = rng.uniform(50, 100, 1000)
score = (
    0.65 * horas
    + 0.035 * frequencia
    + rng.normal(0, 0.8, 1000)
)
aprovado = (score >= 4.2).astype(int)
df = pd.DataFrame({
    "Horas Estudo": horas,
    "Frequência (%)": frequencia,
    "Score": score,
    "Aprovado": aprovado
})
print(df.head(10))
