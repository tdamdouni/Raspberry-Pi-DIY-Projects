cmake_minimum_required(VERSION 2.8.0 FATAL_ERROR)

project(WakeWordAgent)

set( WAKE_WORD_AGENT_SOURCE
        main.cpp
        WakeWordAgent.cpp
        WakeWordEngineFactory.cpp
        WakeWordEngine.cpp
        WakeWordIPCFactory.cpp
        WakeWordIPC.cpp
        WakeWordIPCSocket.cpp
        IPCInterface.cpp
        Logger.cpp
        WakeWordException.cpp
        KittAiSnowboyWakeWordEngine.cpp
        PortAudioWrapper.cpp
        SensoryWakeWordEngine.cpp
        GPIOWakeWordEngine.cpp )

set( WAKE_WORD_AGENT_LIBS
        snowboy-detect
        blas
        portaudio
        asound
        sensory
        wiringPi )

find_package( Threads )
set( CMAKE_THREAD_PREFER_PTHREAD TRUE )

add_executable( wakeWordAgent ${WAKE_WORD_AGENT_SOURCE} )

set_target_properties( wakeWordAgent PROPERTIES COMPILE_FLAGS "-std=c++11" )

target_include_directories( wakeWordAgent PRIVATE ${CMAKE_SOURCE_DIR}/../ext/include )

target_link_libraries( wakeWordAgent ${WAKE_WORD_AGENT_LIBS} )
target_link_libraries( wakeWordAgent ${CMAKE_THREAD_LIBS_INIT} )

add_library( snowboy-detect STATIC IMPORTED )
set_target_properties( snowboy-detect PROPERTIES IMPORTED_LOCATION
  ${CMAKE_SOURCE_DIR}/../ext/lib/libsnowboy-detect.a )

add_library( portaudio STATIC IMPORTED )
set_target_properties( portaudio PROPERTIES IMPORTED_LOCATION
  ${CMAKE_SOURCE_DIR}/../ext/lib/libportaudio.a )

add_library( sensory STATIC IMPORTED )
set_target_properties( sensory PROPERTIES IMPORTED_LOCATION
  ${CMAKE_SOURCE_DIR}/../ext/lib/libsnsr.a )

add_library( blas SHARED IMPORTED )
set_target_properties( blas PROPERTIES IMPORTED_LOCATION
  ${CMAKE_SOURCE_DIR}/../ext/lib/libblas.so.3 )
