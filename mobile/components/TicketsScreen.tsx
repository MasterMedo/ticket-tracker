import React, { useEffect, useState } from 'react';
import { SafeAreaView, StyleSheet, StatusBar } from 'react-native';
import { TicketList } from '../components/TicketList';
import { Ticket } from '../models/Ticket';

export const TicketsScreen = ({ navigation }) => {
  const [tickets, setTickets] = useState<Ticket[]>([]);
  useEffect(() => {
    fetch('http://192.168.0.20:5000/tickets')
      .then((r) => r.json())
      .then((data: Ticket[]) => {
        setTickets(data || []);
      })
      .catch((error) => console.warn(error));
  }, []);

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" />
      <TicketList tickets={tickets} />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#F8F9FB',
  },
});
