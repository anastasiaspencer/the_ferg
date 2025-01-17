# The Ferg - ROS 2 Package

This README outlines the steps to build and launch the `the_ferg` ROS 2 package.

## Prerequisites

Ensure you have ROS 2 Humble installed and your workspace set up.

## Steps to Build and Launch

1. **Navigate to your ROS workspace:**
   ```bash
   cd ~/ros2_ws/
   ```

2. **Source the ROS 2 environment:**
   ```bash
   source /opt/ros/humble/setup.bash
   ```

3. **Change directory to the `the_ferg` package:**
   ```bash
   cd the_ferg/
   ```

4. **Build the package using colcon:**
   ```bash
   colcon build
   ```

5. **Source the install setup file:**
   ```bash
   source install/setup.bash
   ```

6. **Launch the Webots simulation:**
   ```bash
   ros2 launch the_ferg run_webots.launch.py
   ```
## How to change door functionality

1. **Open world file**
   ```bash
   nano FirstFloorStudentCenter.wbt
   ```



2. **Find door node to change**
    ```bash
    Door {
        hidden translation_5 0.0010443992516748768 1.392506505060176e-05 1.1102230246251565e-16
        hidden rotation_5 0 0 -1 9.347074035019101e-05
        translation -12.46 -25.93 0
        position -9.34707386304474e-05
    }
    ```

3. **Add canBeOpen line and set to true or false depending on desired functionality.**
    ```bash
    Door {
        hidden translation_5 0.0010443992516748768 1.392506505060176e-05 1.1102230246251565e-16
        hidden rotation_5 0 0 -1 9.347074035019101e-05
        translation -12.46 -25.93 0
        position -9.34707386304474e-05
        canBeOpen = True
    }
    ```

# Manipulating Lighting in the World File

This guide provides instructions on how to manipulate the lighting of your world file. The two primary types of lights you can work with are `PointLight` and background lights. 

## 1. PointLight

The `PointLight` emits light in all directions from a specific point in 3D space. It can be adjusted through various properties.

### Properties:
- **attenuation**: Controls how light diminishes over distance. It typically has three values: 
  - Constant attenuation
  - Linear attenuation
  - Quadratic attenuation
- **intensity**: Determines the brightness of the light source. Higher values produce brighter light.
- **location**: Sets the position of the light in the 3D space, specified by (x, y, z) coordinates.
- **castShadows**: When set to `TRUE`, the light source will cast shadows.

### Example:
```plaintext
PointLight {
  attenuation 0 0 1  # No constant or linear attenuation; quadratic attenuation only
  intensity 7         # Light brightness
  location 6 2.5 1.8  # Position of the light in 3D space
}
```

## 2. Background Lights

### TexturedBackgroundLight and TexturedBackground

You can set up background lighting using `TexturedBackgroundLight` and `TexturedBackground`. These properties typically affect the overall lighting and appearance of the environment.

### Example:
```plaintext
TexturedBackgroundLight {
  # You can specify light properties here if needed
}

TexturedBackground {
  # You can specify background textures and other properties here
}
```

## 3. Adjusting Lighting

### To modify existing lights:
1. **Change the `intensity`** to make the light brighter or dimmer. 
   ```plaintext
   intensity 10  # Example of increasing brightness
   ```

2. **Change the `location`** to reposition the light.
   ```plaintext
   location 4 3 2  # Moves the light to a new position
   ```

3. **Enable shadows** for more realistic lighting by setting `castShadows` to `TRUE`.
   ```plaintext
   castShadows TRUE  # This light will cast shadows
   ```

## Notes

- Make sure to resolve any warnings or errors that may occur during the build process.
- If you encounter issues, check your setup and configuration.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.
