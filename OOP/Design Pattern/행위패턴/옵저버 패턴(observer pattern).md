# 옵저버 패턴(observer pattern)

옵저버 패턴은 일부 객체들이 다른 객체들에 자신의 상태 변경에 대해 알릴 수 있는 행위 디자인 패턴입니다.

이 패턴은 하나의 객체(Subject)가 다른 객체(Observer)에게 변경 사항을 알려주는 것을 말합니다.





## ex 1)

    interface Subject {
        void registerObserver(Observer o);
        void removeObserver(Observer o);
        void notifyObservers();
    }

    interface Observer {
        void update(int value);
    }

    class ConcreteSubject implements Subject {
        private List<Observer> observers = new ArrayList<>();
        private int value;

        public void setValue(int value) {
            this.value = value;
            notifyObservers();
        }

        @Override
        public void registerObserver(Observer o) {
            observers.add(o);
        }

        @Override
        public void removeObserver(Observer o) {
            observers.remove(o);
        }

        @Override
        public void notifyObservers() {
            for(Observer observer : observers) {
                observer.update(value);
            }
        }
    }

    class ConcreteObserver implements Observer {
        private int value;

        @Override
        public void update(int value) {
            this.value = value;
            System.out.println("Observer: " + value);
        }
    }

    class Main {
        public static void main(String[] args) {
            ConcreteSubject subject = new ConcreteSubject();
            ConcreteObserver observer1 = new ConcreteObserver();
            ConcreteObserver observer2 = new ConcreteObserver();

            subject.registerObserver(observer1);
            subject.registerObserver(observer2);

            subject.setValue(10);
        }
    }


## ex 2) 날씨 예보

하나의 기상 정보를 가지고 있는 WeatherData 객체가 있고, 이 기상 정보를 관찰하는 CurrentConditionsDisplay, ForecastDisplay 가 있다고 가정해보자!


WeatherData

    public class WeatherData {
        private ArrayList<Observer> observers;
        private float temperature;
        private float humidity;
        private float pressure;

        public WeatherData() {
            observers = new ArrayList<Observer>();
        }

        public void registerObserver(Observer o) {
            observers.add(o);
        }

        public void removeObserver(Observer o) {
            int i = observers.indexOf(o);
            if (i >= 0) {
                observers.remove(i);
            }
        }

        public void notifyObservers() {
            for (Observer observer : observers) {
                observer.update(temperature, humidity, pressure);
            }
        }

        public void measurementsChanged() {
            notifyObservers();
        }

        public void setMeasurements(float temperature, float humidity, float pressure) {
            this.temperature = temperature;
            this.humidity = humidity;
            this.pressure = pressure;
            measurementsChanged();
        }
    }

Observer interface

    public interface Observer {
        public void update(float temp, float humidity, float pressure);
    }
  

CurrentConditionsDisplay class
    
    public class CurrentConditionsDisplay implements Observer {
        private float temperature;
        private float humidity;

        public CurrentConditionsDisplay() {
        }

        public void update(float temperature, float humidity, float pressure) {
            this.temperature = temperature;
            this.humidity = humidity;
            display();
        }

        public void display() {
            System.out.println("Current conditions: " + temperature 
                               + "F degrees and " + humidity + "% humidity");
        }
    }    


ForecastDisplay  class
    
    public class ForecastDisplay  implements Observer {
        private float temperature;
        private float humidity;
        

        public ForecastDisplay () {
        }

        public void update(float temperature, float humidity, float pressure) {
            this.temperature = temperature;
            this.humidity = humidity;
            display();
        }

        public void display() {
            System.out.println("Forecast : " + temperature 
                               + "F degrees and " + humidity + "% humidity");
        }
    }    

client

    class Main {
        public static void main(String[] args) {
            WeatherData weatherData = new WeatherData();
            Observer observer1 = new CurrentConditionsDisplay(weatherData);
            Observer observer2 = new ForecastDisplay(weatherData);
            weatherData.addObserver(observer1);
            weatherData.addObserver(observer2);
            weatherData.setMeasurements(51.8, 30 , 999);
        }
    }



### 참고

https://refactoring.guru/ko/design-patterns/observer





