import React from 'react';
import { Text, StyleSheet, View } from 'react-native';

export const TicketListHeader = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Tickets</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginVertical: 10,
    marginHorizontal: 10,
  },
  text: {
    fontSize: 25,
  },
});
