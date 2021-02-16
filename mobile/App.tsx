import 'react-native-gesture-handler';
import React from 'react';
import { SafeAreaView, StyleSheet, StatusBar } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { TicketsScreen } from './components/TicketsScreen';
import { TicketScreen } from './components/TicketScreen';

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Tickets"
          component={TicketsScreen}
          options={{ title: 'Tickets' }}
        />
        <Stack.Screen
          name="Ticket"
          component={TicketScreen}
          options={{ title: 'Ticket' }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

const Stack = createStackNavigator();

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#F8F9FB',
  },
});

export default App;
