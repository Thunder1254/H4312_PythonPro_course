class BuildingErrorForPetro(Exception):
    def __str__(self):
        return f"with so little material the house cannot be built"


def check_material(now_material,min_material, ):
    if now_material >= min_material:
        print("Enough")
    else:
        raise BuildingErrorForPetro
material_user = float(input("Enter material:    "))
check_material(material_user, 300)





