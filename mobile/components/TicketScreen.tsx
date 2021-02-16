import React from 'react';
import { SafeAreaView, Text, StyleSheet } from 'react-native';
import { Ticket } from '../models/Ticket';

interface Props {
  ticket: Ticket;
}

export const TicketScreen = ({ ticket }: Props) => {
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>{ticket.title}</Text>
      <Text style={styles.content}>{ticket.content}</Text>
      <Text style={styles.small}>{ticket.submitter_id}</Text>
      <Text style={styles.small}>{ticket.timestamp}</Text>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#ffffff',
    borderRadius: 15,
    marginHorizontal: 10,
    marginVertical: 10,
  },
  title: {
    fontSize: 25,
  },
  content: {
    fontSize: 18,
  },
  small: {
    fontSize: 16,
  },
});
