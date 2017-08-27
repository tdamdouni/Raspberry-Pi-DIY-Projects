cmake_minimum_required(VERSION 2.8.0 FATAL_ERROR)

project(wakeWordAgentTest)

set( WAKE_WORD_AGENT_TEST_SOURCE
        main.cpp
        testLogger.cpp
        testKittAi.cpp
        testIPCFactory.cpp
        testSensory.cpp
        testGPIO.cpp
        ../src/IPCInterface.cpp
        ../src/KittAiSnowboyWakeWordEngine.cpp
        ../src/Logger.cpp
        ../src/PortAudioWrapper.cpp
        ../src/SensoryWakeWordEngine.cpp
        ../src/GPIOWakeWordEngine.cpp
        ../src/WakeWordAgent.cpp
        ../src/WakeWordEngine.cpp
        ../src/WakeWordEngineFactory.cpp
        ../src/WakeWordException.cpp
        ../src/WakeWordIPC.cpp
        ../src/WakeWordIPCFactory.cpp
        ../src/WakeWordIPCSocket.cpp )

set( WAKE_WORD_AGENT_TEST_LIBS
        snowboy-detect
        blas
        portaudio
        asound
        sensory
        wiringPi )

find_package( Threads )
set( CMAKE_THREAD_PREFER_PTHREAD TRUE )

add_executable( wakeWordAgentTest ${WAKE_WORD_AGENT_TEST_SOURCE} )

set_target_properties( wakeWordAgentTest PROPERTIES COMPILE_FLAGS "-std=c++11" )

target_include_directories( wakeWordAgentTest PRIVATE ${CMAKE_SOURCE_DIR}/../src )
target_include_directories( wakeWordAgentTest PRIVATE ${CMAKE_SOURCE_DIR}/../ext/include )

target_link_libraries( wakeWordAgentTest ${WAKE_WORD_AGENT_TEST_LIBS} )
target_link_libraries( wakeWordAgentTest ${CMAKE_THREAD_LIBS_INIT} )

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
