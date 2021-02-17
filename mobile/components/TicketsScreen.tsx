import React, { useEffect, useState } from 'react';
import {
  Pressable,
  Text,
  SafeAreaView,
  StyleSheet,
  StatusBar,
} from 'react-native';
import { TicketList } from '../components/TicketList';
import { Ticket } from '../models/Ticket';
import { TicketsScreenNavigationProp } from '../models/Navigation';

interface Props {
  navigation: TicketsScreenNavigationProp;
}

export const TicketsScreen = ({ navigation }: Props) => {
  const [tickets, setTickets] = useState<Ticket[]>([]);
  useEffect(() => {
    fetch('http://192.168.0.155:5000/tickets')
      .then((r) => r.json())
      .then((data: Ticket[]) => {
        setTickets(data || []);
      })
      .catch((error) => console.warn(error));
  }, []);

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" />
      <Pressable
        onPress={() => {
          navigation.navigate('TicketCreate', { submitter_id: 5 });
        }}
      >
        <Text>Create Ticket</Text>
      </Pressable>
      <TicketList tickets={tickets} navigation={navigation} />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#F8F9FB',
  },
});
