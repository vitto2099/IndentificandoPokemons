import pandas as pd
import pickle
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

# ──────────────────────────────────────────────
# 1. CARREGAMENTO DOS DADOS
# ──────────────────────────────────────────────
base_credit = pd.read_csv('credit_data.csv')
print("Base de dados:")
print(base_credit.head())
print(f"\nShape: {base_credit.shape}")

# ──────────────────────────────────────────────
# 2. CARREGAMENTO DOS DADOS PRÉ-PROCESSADOS
# ──────────────────────────────────────────────
with open('credit.pkl', 'rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)

print(f"\nTreinamento - X: {X_credit_treinamento.shape} | y: {y_credit_treinamento.shape}")
print(f"Teste       - X: {X_credit_teste.shape} | y: {y_credit_teste.shape}")

# ──────────────────────────────────────────────
# 3. CRIAÇÃO E TREINO DA REDE NEURAL
# ──────────────────────────────────────────────
rede_neural_credit = MLPClassifier(
    max_iter=1500,
    verbose=True,
    tol=0.0000100,
    solver='adam',
    activation='relu',
    hidden_layer_sizes=(20, 20)
)

rede_neural_credit.fit(X_credit_treinamento, y_credit_treinamento)

# ──────────────────────────────────────────────
# 4. PREVISÕES
# ──────────────────────────────────────────────
previsoes = rede_neural_credit.predict(X_credit_teste)

print("\nPrevisões:")
print(previsoes)
print("\nValores reais:")
print(y_credit_teste)

# ──────────────────────────────────────────────
# 5. AVALIAÇÃO DO MODELO
# ──────────────────────────────────────────────
acuracia = accuracy_score(y_credit_teste, previsoes)
print(f"\nAcurácia: {acuracia:.4f} ({acuracia * 100:.2f}%)")

print("\nRelatório de Classificação:")
print(classification_report(y_credit_teste, previsoes))