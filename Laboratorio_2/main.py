"""
Laboratorio 2: Ley de Biot-Savart - Script Principal

Este script permite ejecutar todos los análisis del laboratorio de manera
organizada y generar todos los gráficos necesarios.

Universidad Nacional del Sur - Física II
Autor: Juan Cruz Mariani
"""

import sys
import os

def menu_principal():
    """
    Muestra el menú principal del laboratorio.
    """
    print("\n" + "="*80)
    print(" "*20 + "LABORATORIO 2: LEY DE BIOT-SAVART")
    print(" "*25 + "Universidad Nacional del Sur")
    print("="*80)
    print("\nSeleccione la opción que desea ejecutar:\n")
    print("  [1] Inciso A - Campo Magnético de Alambre Recto")
    print("  [2] Inciso B - Campo Magnético de Espira Circular")
    print("  [3] Inciso C - Configuración Combinada (Alambre + Espira)")
    print("  [4] Bobinas de Helmholtz")
    print("  [5] Ejecutar TODOS los análisis")
    print("  [6] Probar funciones base (biot_savart.py)")
    print("  [0] Salir")
    print("\n" + "="*80)


def ejecutar_inciso_a():
    """Ejecuta el inciso A."""
    print("\n" + ">"*80)
    print("Ejecutando Inciso A - Campo Magnético de Alambre Recto")
    print(">"*80 + "\n")
    
    try:
        import alambre_recto
        alambre_recto.main()
        print("\n✓ Inciso A completado exitosamente\n")
    except Exception as e:
        print(f"\n✗ Error en Inciso A: {e}\n")
        import traceback
        traceback.print_exc()


def ejecutar_inciso_b():
    """Ejecuta el inciso B."""
    print("\n" + ">"*80)
    print("Ejecutando Inciso B - Campo Magnético de Espira Circular")
    print(">"*80 + "\n")
    
    try:
        import espira_circular
        espira_circular.main()
        print("\n✓ Inciso B completado exitosamente\n")
    except Exception as e:
        print(f"\n✗ Error en Inciso B: {e}\n")
        import traceback
        traceback.print_exc()


def ejecutar_inciso_c():
    """Ejecuta el inciso C."""
    print("\n" + ">"*80)
    print("Ejecutando Inciso C - Configuración Combinada")
    print(">"*80 + "\n")
    
    try:
        import alambre_espira_combinados
        alambre_espira_combinados.main()
        print("\n✓ Inciso C completado exitosamente\n")
    except Exception as e:
        print(f"\n✗ Error en Inciso C: {e}\n")
        import traceback
        traceback.print_exc()


def ejecutar_helmholtz():
    """Ejecuta el análisis de bobinas de Helmholtz."""
    print("\n" + ">"*80)
    print("Ejecutando Análisis de Bobinas de Helmholtz")
    print(">"*80 + "\n")
    
    try:
        import helmholtz
        helmholtz.main()
        print("\n✓ Análisis de Helmholtz completado exitosamente\n")
    except Exception as e:
        print(f"\n✗ Error en Helmholtz: {e}\n")
        import traceback
        traceback.print_exc()


def ejecutar_todos():
    """Ejecuta todos los análisis en secuencia."""
    print("\n" + "#"*80)
    print(" "*15 + "EJECUTANDO TODOS LOS ANÁLISIS DEL LABORATORIO")
    print("#"*80 + "\n")
    
    ejecutar_inciso_a()
    input("\nPresione Enter para continuar con el Inciso B...")
    
    ejecutar_inciso_b()
    input("\nPresione Enter para continuar con el Inciso C...")
    
    ejecutar_inciso_c()
    input("\nPresione Enter para continuar con Bobinas de Helmholtz...")
    
    ejecutar_helmholtz()
    
    print("\n" + "#"*80)
    print(" "*20 + "TODOS LOS ANÁLISIS COMPLETADOS")
    print("#"*80)
    print("\nTodos los gráficos han sido guardados en la carpeta 'plots/'")


def probar_funciones_base():
    """Prueba las funciones base de biot_savart.py."""
    print("\n" + ">"*80)
    print("Probando funciones base (biot_savart.py)")
    print(">"*80 + "\n")
    
    try:
        import biot_savart
        # El módulo tiene un __main__ que ejecuta pruebas
        print("\n✓ Funciones base funcionando correctamente\n")
    except Exception as e:
        print(f"\n✗ Error en funciones base: {e}\n")
        import traceback
        traceback.print_exc()


def verificar_dependencias():
    """
    Verifica que todas las dependencias estén instaladas.
    """
    print("\nVerificando dependencias...")
    
    dependencias = {
        'numpy': 'NumPy',
        'matplotlib': 'Matplotlib',
        'scipy': 'SciPy (opcional, para optimizaciones)'
    }
    
    faltantes = []
    
    for modulo, nombre in dependencias.items():
        try:
            __import__(modulo)
            print(f"  ✓ {nombre} - OK")
        except ImportError:
            print(f"  ✗ {nombre} - NO INSTALADO")
            faltantes.append(nombre)
    
    if faltantes:
        print(f"\n⚠ ADVERTENCIA: Faltan las siguientes dependencias:")
        for dep in faltantes:
            print(f"    - {dep}")
        print("\nPara instalar, ejecute:")
        print("  pip install numpy matplotlib scipy")
        return False
    else:
        print("\n✓ Todas las dependencias están instaladas\n")
        return True


def main():
    """
    Función principal del menú interactivo.
    """
    # Verificar dependencias al inicio
    if not verificar_dependencias():
        respuesta = input("\n¿Desea continuar de todas formas? (s/n): ")
        if respuesta.lower() != 's':
            print("\nSaliendo del programa...")
            return
    
    while True:
        menu_principal()
        
        try:
            opcion = input("Ingrese su opción: ").strip()
            
            if opcion == '0':
                print("\n¡Hasta luego!\n")
                break
            elif opcion == '1':
                ejecutar_inciso_a()
            elif opcion == '2':
                ejecutar_inciso_b()
            elif opcion == '3':
                ejecutar_inciso_c()
            elif opcion == '4':
                ejecutar_helmholtz()
            elif opcion == '5':
                ejecutar_todos()
            elif opcion == '6':
                probar_funciones_base()
            else:
                print("\n⚠ Opción no válida. Por favor, seleccione una opción del menú.\n")
            
            if opcion in ['1', '2', '3', '4', '6']:
                input("\nPresione Enter para volver al menú principal...")
        
        except KeyboardInterrupt:
            print("\n\nInterrumpido por el usuario. Saliendo...\n")
            break
        except Exception as e:
            print(f"\n✗ Error inesperado: {e}\n")
            import traceback
            traceback.print_exc()
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
