import 'react-native-gesture-handler';
import React from 'react';
import { SafeAreaView, StyleSheet, StatusBar } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { TicketsScreen } from './components/TicketsScreen';
import { TicketScreen } from './components/TicketScreen';
import { TicketCreateScreen } from './components/TicketCreateScreen';
import { NavigationParamList } from './models/Navigation';

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Tickets">
        <Stack.Screen name="Tickets" component={TicketsScreen} />
        <Stack.Screen
          name="Ticket"
          component={TicketScreen}
          options={{ title: 'Ticket' }}
        />
        <Stack.Screen name="TicketCreate" component={TicketCreateScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

const Stack = createStackNavigator<NavigationParamList>();

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#F8F9FB',
  },
});

export default App;
