import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import moment from 'moment';
import { Ticket } from '../models/Ticket';

interface Props {
  ticket: Ticket;
}

export const TicketRow = ({ ticket }: Props) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{ticket.title}</Text>
      <Text style={styles.small}>{moment.utc(ticket.timestamp).fromNow()}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 1,
    backgroundColor: '#E9EDF0',
    padding: 20,
    marginVertical: 10,
    marginHorizontal: 10,
    borderRadius: 15,
  },
  title: {
    fontSize: 20,
  },
  small: {
    fontSize: 16,
    color: '#939597',
  },
});
