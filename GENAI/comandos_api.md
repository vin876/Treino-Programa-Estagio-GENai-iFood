ComandosGemini API:
model = genai.GenerativeModel("gemini-1.5-flash")
model.generate_content("Olá")


Como enviar documentos:

model.generate_content(
    ["Explique esse documento:", arquivo_pdf]
)


Pedindo JSON estruturado:

model.generate_content(
    "Responda apenas em JSON com {risco, oportunidade}"
)
