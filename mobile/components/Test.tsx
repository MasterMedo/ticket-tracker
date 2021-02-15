import React from 'react';
import {SafeAreaView, Button, Alert} from 'react-native';

export const Test = () => {
  return (
    <SafeAreaView style={styles.container}>
      <Button
        onPress={() => Alert.alert("")}
        title="can't touch this"
        color="#841584"
        accessibilityLabel="Learn more about this purple button"
      />
    </SafeAreaView>
  );
};
