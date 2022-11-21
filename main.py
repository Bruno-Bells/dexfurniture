from browser import document, window, console
from pyweb3d.pyweb3d import *
from javascript import UNDEFINED as undefined, NULL as null
import json


GLTFLoader = window.THREE.GLTFLoader.new
OrbitControls = window.THREE.OrbitControls.new

#Variables for setup

camera = None
renderer = None
scene = None
controls = None
sofa = None
container = document.getElementById('myScene')
spin_sofa = True

def init():
    global camera
    global renderer
    global scene
    global container
    global controls

    w = container.offsetWidth
    h = container.offsetHeight

    #Create scene
    scene = Scene()
    

    fov = 45
    aspect = w / h
    near = 1
    far = 1500

    #Camera setup
    camera = PerspectiveCamera(fov, aspect, near, far)
    camera.position.x = 0
    camera.position.y = 1
    camera.position.z = 10

    ambientLight = AmbientLight('grey', 1)
    scene.add( ambientLight )

    spotLight = SpotLight( 0xffffff )
    spotLight.position.set( 10, 10, 10 )
    scene.add( spotLight )

    # DirectLight = DirectionalLight()
    # DirectLight.position.set( 10, 10, 10 )
    # scene.add( DirectLight )

    #Renderer
    renderer = WebGLRenderer( { 'alpha': True, 'antialias': True } )
    renderer.setClearColor( 0x000000, 0 )
    renderer.setPixelRatio( window.devicePixelRatio )
    renderer.setSize( w, h )
    renderer.outputEncoding = sRGBEncoding

    container.appendChild( renderer.domElement )

    controls = OrbitControls(camera, renderer.domElement)
    controls.minDistance  = 8
    controls.maxDistance  = 10

    # Textures
    textureLoader = TextureLoader()

    texture1 = textureLoader.load('assets/models/couch_textures/Base/texture1.jpg')
    texture1.wrapS = RepeatWrapping
    texture1.wrapT = RepeatWrapping
    texture1.name = 'texture1'

    texture2 = textureLoader.load('assets/models/couch_textures/Base/texture2.jpg')
    texture2.wrapS = RepeatWrapping
    texture2.wrapT = RepeatWrapping
    texture2.name = 'texture2'

    texture3 = textureLoader.load('assets/models/couch_textures/Base/texture3.jpg')
    texture3.wrapS = RepeatWrapping
    texture3.wrapT = RepeatWrapping
    texture3.name = 'texture3'

    texture4 = textureLoader.load('assets/models/couch_textures/Base/texture4.jpg')
    texture4.wrapS = RepeatWrapping
    texture4.wrapT = RepeatWrapping
    texture4.name = 'texture4'

    texture5 = textureLoader.load('assets/models/couch_textures/Base/texture5.jpg')
    texture5.wrapS = RepeatWrapping
    texture5.wrapT = RepeatWrapping
    texture5.name = 'texture5'

    texture6 = textureLoader.load('assets/models/couch_textures/Base/texture6.jpg')
    texture6.wrapS = RepeatWrapping
    texture6.wrapT = RepeatWrapping
    texture6.name = 'texture6'

    texture7 = textureLoader.load('assets/models/couch_textures/Base/texture7.jpg')
    texture7.wrapS = RepeatWrapping
    texture7.wrapT = RepeatWrapping
    texture7.name = 'texture7'

    texture8 = textureLoader.load('assets/models/couch_textures/Base/texture8.jpg')
    texture8.wrapS = RepeatWrapping
    texture8.wrapT = RepeatWrapping
    texture8.name = 'texture8'

    allTextures = [texture1, texture2, texture3, texture4, texture5, texture6, texture7, texture8]

    # materials
    baseMaterial = MeshStandardMaterial( {
                "uuid": 1, "type": "MeshStandardMaterial", "name": "new_sofa_Cloth",
                "color": 16777215, "roughness": 0.8040408205773457, "metalness": 0, "emissive": 0,
                "map": texture8, "normalScale": [1,1],"envMapIntensity": 1,
                "side": 2, "depthFunc": 3, "depthTest": True, "depthWrite": True, "colorWrite": True, 
                "stencilWrite": False, "stencilWriteMask": 255, "stencilFunc": 519, "stencilRef": 0, 
                "stencilFuncMask": 255, "stencilFail": 7680, "stencilZFail": 7680, "stencilZPass": 7680,
                } )
    
    FeetMaterial = MeshStandardMaterial( {
            "uuid": 2, "type": "MeshStandardMaterial", "name": "new_Feet", "color": 657930, "roughness": 0.9888825370832454,
            "metalness": 0, "emissive": 0, "envMapIntensity": 1, "side": 2, "depthFunc": 3, "depthTest": True, 
            "depthWrite": True, "colorWrite": True, "stencilWrite": False, "stencilWriteMask": 255, "stencilFunc": 519, 
            "stencilRef": 0, "stencilFuncMask": 255, "stencilFail": 7680, "stencilZFail": 7680,"stencilZPass": 7680
            } )
    
    sideFrameMaterial = MeshStandardMaterial( {
                "uuid": 3, "type": "MeshStandardMaterial", "name": "new_sofa_Cloth",
                "color": 16777215, "roughness": 0.8040408205773457, "metalness": 0, "emissive": 0,
                "map": texture8, "normalScale": [1,1],"envMapIntensity": 1,
                "side": 2, "depthFunc": 3, "depthTest": True, "depthWrite": True, "colorWrite": True, 
                "stencilWrite": False, "stencilWriteMask": 255, "stencilFunc": 519, "stencilRef": 0, 
                "stencilFuncMask": 255, "stencilFail": 7680, "stencilZFail": 7680, "stencilZPass": 7680,
                } )
    
    seatMaterial = MeshStandardMaterial( {
                "uuid": 4, "type": "MeshStandardMaterial", "name": "new_sofa_Cloth",
                "color": 16777215, "roughness": 0.8040408205773457, "metalness": 0, "emissive": 0,
                "map": texture8, "normalScale": [1,1],"envMapIntensity": 1,
                "side": 2, "depthFunc": 3, "depthTest": True, "depthWrite": True, "colorWrite": True, 
                "stencilWrite": False, "stencilWriteMask": 255, "stencilFunc": 519, "stencilRef": 0, 
                "stencilFuncMask": 255, "stencilFail": 7680, "stencilZFail": 7680, "stencilZPass": 7680,
                } )
    
    side_stripMaterial = MeshStandardMaterial( {"uuid": 5, "type": "MeshStandardMaterial", "name": "new_strip_garnish", 
        "color": 14530612, "roughness": 0.8012455753874624, "metalness": 0, "emissive": 0, "envMapIntensity": 1, 
        "side": 2, "depthFunc": 3, "depthTest": True, "depthWrite": True, "colorWrite": True, "stencilWrite": False, "stencilWriteMask": 255,
        "stencilFunc": 519, "stencilRef": 0, "stencilFuncMask": 255, "stencilFail": 7680, "stencilZFail": 7680,"stencilZPass": 7680
        })
    
    cushion003Material = MeshStandardMaterial( {
                "uuid": 6, "type": "MeshStandardMaterial", "name": "new_sofa_Cloth",
                "color": 16777215, "roughness": 0.8040408205773457, "metalness": 0, "emissive": 0,
                "map": texture8, "normalScale": [1,1],"envMapIntensity": 1,
                "side": 2, "depthFunc": 3, "depthTest": True, "depthWrite": True, "colorWrite": True, 
                "stencilWrite": False, "stencilWriteMask": 255, "stencilFunc": 519, "stencilRef": 0, 
                "stencilFuncMask": 255, "stencilFail": 7680, "stencilZFail": 7680, "stencilZPass": 7680,
                } )
    
    cushion004Material = MeshStandardMaterial( {
                "uuid": 7, "type": "MeshStandardMaterial", "name": "new_sofa_Cloth",
                "color": 16777215, "roughness": 0.8040408205773457, "metalness": 0, "emissive": 0,
                "map": texture8, "normalScale": [1,1],"envMapIntensity": 1,
                "side": 2, "depthFunc": 3, "depthTest": True, "depthWrite": True, "colorWrite": True, 
                "stencilWrite": False, "stencilWriteMask": 255, "stencilFunc": 519, "stencilRef": 0, 
                "stencilFuncMask": 255, "stencilFail": 7680, "stencilZFail": 7680, "stencilZPass": 7680,
                } )
    
    cushion005Material = MeshStandardMaterial( {
                "uuid": 8, "type": "MeshStandardMaterial", "name": "new_sofa_Cloth",
                "color": 16777215, "roughness": 0.8040408205773457, "metalness": 0, "emissive": 0,
                "map": texture8, "normalScale": [1,1],"envMapIntensity": 1,
                "side": 2, "depthFunc": 3, "depthTest": True, "depthWrite": True, "colorWrite": True, 
                "stencilWrite": False, "stencilWriteMask": 255, "stencilFunc": 519, "stencilRef": 0, 
                "stencilFuncMask": 255, "stencilFail": 7680, "stencilZFail": 7680, "stencilZPass": 7680,
                } )
    
    cushionSmallMaterial = MeshStandardMaterial({
            "uuid": 9, "type": "MeshStandardMaterial", "name": "new_cushoinsmall", "color": 16777215,
            "roughness": 0.8211145618000169, "metalness": 0, "emissive": 0, "map": texture5, "envMapIntensity": 1,
            "side": 2, "depthFunc": 3, "depthTest": True, "depthWrite": True, "colorWrite": True, 
            "stencilWrite": False, "stencilWriteMask": 255, "stencilFunc": 519, "stencilRef": 0, 
            "stencilFuncMask": 255, "stencilFail": 7680, "stencilZFail": 7680, "stencilZPass": 7680,

    })
    
    cushionSmall001Material = MeshStandardMaterial({
            "uuid": 10, "type": "MeshStandardMaterial", "name": "new_cushoinsmall", "color": 16777215,
            "roughness": 0.8211145618000169, "metalness": 0, "emissive": 0, "map": texture6, "envMapIntensity": 1,
            "side": 2, "depthFunc": 3, "depthTest": True, "depthWrite": True, "colorWrite": True, 
            "stencilWrite": False, "stencilWriteMask": 255, "stencilFunc": 519, "stencilRef": 0, 
            "stencilFuncMask": 255, "stencilFail": 7680, "stencilZFail": 7680, "stencilZPass": 7680,

    })
    
    cushionSmall002Material = MeshStandardMaterial({
            "uuid": 11, "type": "MeshStandardMaterial", "name": "new_cushoinsmall", "color": 16777215,
            "roughness": 0.8211145618000169, "metalness": 0, "emissive": 0, "map": texture7, "envMapIntensity": 1,
            "side": 2, "depthFunc": 3, "depthTest": True, "depthWrite": True, "colorWrite": True, 
            "stencilWrite": False, "stencilWriteMask": 255, "stencilFunc": 519, "stencilRef": 0, 
            "stencilFuncMask": 255, "stencilFail": 7680, "stencilZFail": 7680, "stencilZPass": 7680,

    })

    basicInfo = document.getElementById('basicInfo')
    brandinfo = document.getElementById('brandinfo')
    brandinfo1 = document.getElementById('brandinfo1')
    basicInfo_btn = document.getElementById('basicInfo_btn')
    show_basicInfo = document.getElementById('show_basicInfo')    
    def basicInfo_btn_ev(ev):
        global spin_sofa
        basicInfo.style.visibility = "hidden"
        brandinfo.style.visibility = "hidden"
        brandinfo1.style.visibility = "hidden"
        spin_sofa = False
    def show_basicInfo_ev(ev):
        global spin_sofa
        basicInfo.style.visibility = "visible"
        brandinfo.style.visibility = "visible"
        brandinfo1.style.visibility = "visible"
        spin_sofa = True
    basicInfo_btn.addEventListener('click', basicInfo_btn_ev)
    show_basicInfo.addEventListener('click', show_basicInfo_ev)

    start_spin = document.getElementById('start_spin')
    stop_spin = document.getElementById('stop_spin')

    def start_spin_ev(ev):
        global spin_sofa
        spin_sofa = True

    def stop_spin_ev(ev):
        global spin_sofa
        spin_sofa = False
    
    start_spin.addEventListener('click', start_spin_ev)
    stop_spin.addEventListener('click', stop_spin_ev)

    # Update Materials
    sideStripColorInput = document.getElementById( 'side-strip-color' )
    def sideStripColorInput_ev(ev):
        side_stripMaterial.color.set( ev.target.value )
    sideStripColorInput.addEventListener( 'input', sideStripColorInput_ev)

    feetColorInput = document.getElementById('feet-color')
    def feetColorInput_ev(ev):
        FeetMaterial.color.set(ev.target.value)
    feetColorInput.addEventListener( 'input', feetColorInput_ev)

    def ChangeTexture(src_string):
        src_string_list = src_string.split()
        material_name = src_string_list[0]
        texture_name = src_string_list[1]

        def get_texture():
            base_texture = None
            for item in allTextures:
                if item.name == texture_name:
                    base_texture = item
            return base_texture

        if material_name.startswith('Base'):
            material_texture = get_texture()
            baseMaterial.map = material_texture
        elif material_name.startswith('Frame'):
             material_texture = get_texture()
             sideFrameMaterial.map = material_texture
        elif material_name.startswith('Seat'):
            material_texture = get_texture()
            seatMaterial.map = material_texture
        elif material_name.startswith('Back1'):
            material_texture = get_texture()
            cushion003Material.map = material_texture
        elif material_name.startswith('Back2'):
            material_texture = get_texture()
            cushion004Material.map = material_texture
        elif material_name.startswith('Back3'):
            material_texture = get_texture()
            cushion005Material.map = material_texture
        elif material_name.startswith('Throw1'):
            material_texture = get_texture()
            cushionSmallMaterial.map = material_texture
        elif material_name.startswith('Throw2'):
            material_texture = get_texture()
            cushionSmall001Material.map = material_texture
        elif material_name.startswith('Throw3'):
            material_texture = get_texture()
            cushionSmall002Material.map = material_texture
        else:
            console.log(len(material_name))


    def texture_Input_ev(ev):
        try:
            texture = ev.target.alt
            ChangeTexture(texture)
        except:
            ...

    document.getElementById('offcanvasScrolling').addEventListener('click', texture_Input_ev)

    #Load Model
    loader = GLTFLoader()

    def loadGLTF(gltf):
        global sofa
        sofa = gltf.scene
        sofa.scale.setScalar(3.2 )
        # center 
        box = Box3().setFromObject( sofa )
        center = box.getCenter( Vector3() )
        sofa.position.x += ( sofa.position.x - center.x )
        sofa.position.y += ( sofa.position.y - center.y - 0.3)
        sofa.position.z += ( sofa.position.z - center.z )

        Base = sofa.getObjectByName('Base')
        Feet = sofa.getObjectByName('Feet')
        sideFrame = sofa.getObjectByName('sideFrame')
        seat = sofa.getObjectByName('seat')
        side_strip = sofa.getObjectByName('side_strip')
        cushion003 = sofa.getObjectByName('cushion003')
        cushion004 = sofa.getObjectByName('cushion004')
        cushion005 = sofa.getObjectByName('cushion005')
        cushionSmall = sofa.getObjectByName('cushionSmall')
        cushionSmall001 = sofa.getObjectByName('cushionSmall001')
        cushionSmall002 = sofa.getObjectByName('cushionSmall002')
        
        # Apply Maps
        Base.children[0]['material'] = baseMaterial # Base
        Feet.children[0]['material'] = FeetMaterial # Feet
        sideFrame.children[0]['material'] = sideFrameMaterial # Frame
        seat.children[0]['material'] = seatMaterial # Seat
        side_strip.children[0]['material'] = side_stripMaterial # side strips
        cushion003.children[0]['material'] = cushion003Material # Back 1
        cushion004.children[0]['material'] = cushion004Material # Back 2
        cushion005.children[0]['material'] = cushion005Material # Back 3
        cushionSmall.children[0]['material'] = cushionSmallMaterial # Throw 1
        cushionSmall.children[1]['material'] = cushionSmallMaterial # Throw 1
        cushionSmall001.children[0]['material'] = cushionSmall001Material # Throw 2
        cushionSmall001.children[1]['material'] = cushionSmall001Material # Throw 2
        cushionSmall002.children[1]['material'] = cushionSmall002Material # Throw 3
        cushionSmall002.children[0]['material'] = cushionSmall002Material # Throw 3
        console.log(sofa)

        scene.add( sofa )
        animate(0)

    def onError(error):
        print(error)

    # loader.load( 'assets/models/couch_sofa.glb', loadGLTF, undefined, onError)
    loader.load( 'assets/models/couch_gltf/scene.gltf', loadGLTF, undefined, onError)

def onWindowResize(resize):
    global container
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()

    renderer.setSize( container.offsetWidth, container.offsetHeight )

window.addEventListener( 'resize', onWindowResize )

def animate(time):
    global controls
    window.requestAnimationFrame( animate )
    renderer.render( scene, camera )
    if spin_sofa:
        sofa.rotation.y += 0.005

    controls.update()

    
init()