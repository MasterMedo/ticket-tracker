import React from 'react';
import {StyleSheet, Text, View} from 'react-native';
import moment from 'moment';
import {Ticket} from '../models/Ticket';

interface Props {
  ticket: Ticket;
}

export const TicketRow = ({ticket}: Props) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{ticket.title}</Text>
      <Text style={styles.small}>{moment.utc(ticket.timestamp).fromNow()}</Text>
      <Text style={styles.small}>{ticket.submitter_id}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 1,
    backgroundColor: '#AAAAAA',
    padding: 20,
    marginVertical: 8,
    marginHorizontal: 6,
  },
  title: {
    fontSize: 25,
  },
  small: {
    fontSize: 16,
  },
});
