## build.gradle 설정

    ......
    sourceSets {
    	test {
    		java {
    			srcDirs 'src/test/kotlin', 'src/test/java'
    		}
    		resources {
    			srcDirs 'src/test/resources'
    		}
    	}
    }
