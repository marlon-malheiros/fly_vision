# Published-flow arithmetic audit correction R2

1 November 2026. V1 successfully loaded the original 45,669-node network and all 34 decoder input types, then executed the first stationary trajectory. Its independent decoder check failed before comparison because the PyPI 1.2.0 release stores decoder u/v coordinates as NumPy arrays, while the checker called Tensor.cpu(). Preserve V1's failure, methods, initial freeze and log under results/neural_model_options_v1; preserve the preceding missing-YAML setup failure separately.

R2 converts the native coordinate arrays using numpy.asarray. No neural source, parameter, input, scientific criterion or tolerance changes. Execute the identical 14 controls in results/neural_model_options_r2 with a new source freeze. The first V1 run did not produce an accepted numerical or physiological result. This is an audit implementation correction, not evidence that the neural model failed its motion task.
