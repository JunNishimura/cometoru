<template>
    <div id="idea__overview-section">
        <div class="idea__overview-container">
            <IdeaPropertyContainer id="idea__overview-mark" title="概要">
                <template #content>
                    <p>{{ overview }}</p>
                </template>
            </IdeaPropertyContainer>
            <IdeaPropertyContainer title="ターゲット">
                <template #content>
                    <p>{{ target }}</p>
                </template>
            </IdeaPropertyContainer>
            <IdeaPropertyContainer title="背景">
                <template #content>
                    <p>{{ background }}</p>
                </template>
            </IdeaPropertyContainer>
            <IdeaPropertyContainer title="価値創造">
                <template #content>
                    <p>{{ value }}</p>
                </template>
            </IdeaPropertyContainer>
            <IdeaPropertyContainer title="情熱">
                <template #content>
                    <p>{{ passion }}</p>
                </template>
            </IdeaPropertyContainer>
        </div>
    </div>
</template>

<script>
import IdeaPropertyContainer from '@/components/Idea/Detail/IdeaPropertyContainer.vue';

export default {
    components: {
        IdeaPropertyContainer,
    },
    props: ['overview', 'target', 'background', 'value', 'passion']
}
</script>