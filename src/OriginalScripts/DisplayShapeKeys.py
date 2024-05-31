from pyfbsdk import*

def displayShapeList(model):
    shapelist = list()
    for shapes in model.PropertyList:
        if type(shapes) == pyfbsdk.FBPropertyAnimatableDouble:
            shapelist.append(shapes.Name)
    separator = ","
    shapestring = separator.join(shapelist)
    if shapestring != "":
        print(model.Name.rjust(12), ":", shapestring)

def SearchShapes(model):
    if len(model.Children) > 0:
        for child in model.Children:
            if type(child) == pyfbsdk.FBModel:
                displayShapeList(child)
            SearchShapes(child)
            
SearchShapes(FBSystem().Scene.RootModel)



def ShapeKey(chara:FBCharacter, option):
    ShapeKeyList = list()
    meshList = FBModelList()
    chara.GetSkinModelList(meshList)
    count = 0
    for mesh in meshList:
        geo = mesh.Geometry
        for i in range(geo.ShapeGetCount()):
            name = geo.ShapeGetName(i)
            if not name in ShapeKeyList:
                ShapeKeyList.append(name)
            else:
                count += 1