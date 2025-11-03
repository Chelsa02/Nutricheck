
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function MealCard({meal, showDetails}) {
  return (
    <View style={styles.card}>
      <Text style={styles.title}>{meal.name}</Text>
      <Text>{meal.calories} kcal • {meal.type}</Text>
      {showDetails && <Text style={{marginTop:6}}>{meal.description}</Text>}
    </View>
  );
}

const styles = StyleSheet.create({
  card:{padding:12, borderWidth:1, borderColor:'#e5e5e5', borderRadius:8, marginBottom:12},
  title:{fontWeight:'700', fontSize:16}
});
