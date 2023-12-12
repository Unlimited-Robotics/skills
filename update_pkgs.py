import subprocess

def execute_main(pkg_name, versions, short_desc, homepage):
    #delete
    env = {
        "PKG_ACTION": "DELETE",
        "PKG_NAME": pkg_name
    }
    subprocess.run(['python3', '.github/actions.py'], env=env)
    print("Package {} deleted".format(pkg_name))
    
    #register
    env = {
        "PKG_ACTION": "REGISTER",
        "PKG_NAME": pkg_name,
        "PKG_VERSION": versions[0],
        "PKG_AUTHOR": 'Unlimited Robotics',
        "PKG_SHORT_DESC": short_desc,
        "PKG_HOMEPAGE": homepage
    }
    subprocess.run(['python3', '.github/actions.py'], env=env)
    print("Package {} registered".format(pkg_name))
    
    #update
    for version in versions[1:]:
        env = {
            "PKG_ACTION": "UPDATE",
            "PKG_NAME": pkg_name,
            "PKG_VERSION": version
        }
        subprocess.run(['python3', '.github/actions.py'], env=env)
        print("Package {} updated to version {}".format(pkg_name, version))
    print("Package {} Done".format(pkg_name))



if __name__ == "__main__":
    # approach_to_tags
    pkg_name = "approach_to_tags"
    versions = ["1.0.1", "2.0.0", "2.0.1.dev", "2.0.2.dev"] 
    short_desc = 'Approaches to a apriltag using different cameras.'
    homepage = 'https://github.com/Unlimited-Robotics/skill_approach_to_tags'
    execute_main(pkg_name, versions, short_desc, homepage)
    
    # approach_to_something
    pkg_name = "approach_to_something"
    versions = ["0.6.0", "0.6.1.dev0", "0.6.2.dev"] 
    short_desc = 'Approaches to something given by a cv model.'
    homepage = 'https://github.com/Unlimited-Robotics/skill_approach_to_something'
    execute_main(pkg_name, versions, short_desc, homepage)
    
    # attach_to_cart
    pkg_name = "attach_to_cart"
    versions = ["0.1.2", "0.1.3", "0.1.4"]
    short_desc = 'Uses apriltags to move to a cart, rotates and attach to it.'
    homepage = 'https://github.com/Unlimited-Robotics/skill_attach_to_cart'
    execute_main(pkg_name, versions, short_desc, homepage)
    
    # dock_to_charger
    pkg_name = "dock_to_charger"
    versions = ["0.0.1"]
    short_desc = 'Approaches to a charger and docks to it.'
    homepage = 'https://github.com/Unlimited-Robotics/skill_dock_to_charger'
    execute_main(pkg_name, versions, short_desc, homepage)
    
    # test_skill
    pkg_name = "test_skill"
    versions = ["0.1.0", "0.1.1.dev", "0.1.2.dev", "0.2.1.dev"]
    short_desc = 'Test skill for testing purposes.'
    homepage = 'https://github.com/Unlimited-Robotics/skill_test_skill'
    execute_main(pkg_name, versions, short_desc, homepage)
    
    
