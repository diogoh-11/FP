# coding: utf-8
# This function computes the body mass index (BMI),
# given the height (in meter) and weight (in kg) of a person.return bmi
def bodyMassIndex(altura, peso):
    bmi = peso / (altura ** 2)
    return bmi
    


# This function returns the BMI category acording to this table:bodyMassIndex(altura,peso)
# BMI:        <18.5         [18.5, 25[      [25, 30[      30 or greater 
# Category:   Underweight   Normal weight   Overweight    Obesity 

def bmiCategory(bmi):
    assert bmi>0
    bmiCategory = "magro"
    if 18.5 <= bmi < 25:
      bmiCategory = "saudavel"
    elif 25 <= bmi < 30:
      bmiCategory = "Forte"
    elif bmi > 30:
      bmiCategory = "Obeso"
    return bmiCategory


    # Complete the function definition...
    ...


# This is the main function
def main():
    print("Índice de Massa Corporal")
    
    altura = float(input("Altura (m)? "))
    if altura < 0:
        print("ERRO: altura inválida!")
        exit(1)

    peso = float(input("Peso (kg)? "))
    if peso < 0:
        print("ERRO: peso inválido!")   
        exit(1)
    bmi = peso / (altura ** 2) 


    # Complete the function calls...
    bodyMassIndex(altura, peso)
    imc = bodyMassIndex(altura,peso)
    cat = bmiCategory(bmi)

    print("BMI: {:.2f} kg/m2".format(imc))
    print("BMI category:", cat)


# Program starts executing here
main()

